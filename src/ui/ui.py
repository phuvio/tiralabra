import os.path
import random
from tkinter import Tk, ttk, constants, Listbox
from tkinter import filedialog as fd
from midi.midi import midi_to_string, string_to_midi
from trie.trie import Trie


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka"""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan

        Args:
            root: Tkinter-elemnetti, jonka sisään käyttöliittymä alustetaan
        """

        self._root = root
        self._current_view = None
        self._trie = Trie()
        self._select_prefix = None
        self._content = None
        self._generated_music = []

    def _select_file(self):
        """Avaa valitun midi-tiedoston ja tallentaa sen nuotit Trie-tietorakenteeseen
        """
        file = fd.askopenfile(
            mode='r',
            filetypes=[('Midi-tiedostot', '*.midi')],
            initialdir="./data")

        self._content = list(midi_to_string(os.path.abspath(file.name)).split())

        for i in range(2, 7):
            for j in range(0, len(self._content) - i):
                self._trie.add_list_to_trie(self._content[j:j+i])

    def _generate_music(self):
        """Generoi musiikkia valitun prefix-pituuden mukaan
        """
        prefix_lenght = self._select_prefix.curselection()[0] + 1
        prefix = []

        for i in range(0, prefix_lenght):
            prefix.append(self._content[i])

        self._generated_music = prefix[:]

        while len(self._generated_music) < len(self._content):
            if self._trie.search_given_prefix(prefix):
                notes = list(self._trie.return_choices(prefix).keys())
                weights = list(self._trie.return_choices(prefix).values())

                next_note = random.choices(notes, weights)

                self._generated_music.append(next_note[0])
                prefix.append(next_note[0])
                prefix.pop(0)

            else:
                break
        
        generated_music_to_string = " ".join(self._generated_music)
        generated_music_to_midi = string_to_midi(generated_music_to_string)
        generated_music_to_midi.write("midi", "./data/generated.midi")
        

    def start(self):
        """Käynnistää käyttöliittymän"""

        label = ttk.Label(master=self._root,
                          text="Musiikin generointi Markovin ketjun avulla",
                          font=('Helvetica', 14, 'bold'))

        label.pack(padx=5, pady=5)

        open_button = ttk.Button(
            self._root,
            text="Avaa midi-tiedosto",
            command=self._select_file
        )
        open_button.pack(padx=5, pady=10, expand=False)

        text=ttk.Label(text="Valitse kuinka monta nuottia generoinnissa käytetään")
        text.pack()

        self._select_prefix = Listbox(
            self._root,
            width=5,
            height=0
        )
        self._select_prefix.insert(1, "    1")
        self._select_prefix.insert(2, "    2")
        self._select_prefix.insert(3, "    3")
        self._select_prefix.insert(4, "    4")
        self._select_prefix.insert(5, "    5")
        self._select_prefix.pack(padx=5, pady=5)

        generate_button = ttk.Button(
            self._root,
            text="Generoi musiikkia",
            command=self._generate_music
        )
        generate_button.pack(padx=5, pady=5, expand=False)

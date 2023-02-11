import os.path
from tkinter import Tk, ttk, constants
from tkinter import filedialog as fd
from midi.midi import midi_to_string
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

    def _select_file(self):
        """Avaa valitun midi-tiedoston ja tallentaa sen nuotit Trie-tietorakenteeseen
        """
        file = fd.askopenfile(
            mode='r',
            filetypes=[('Midi-tiedostot', '*.midi')])

        content = list(midi_to_string(os.path.abspath(file.name)).split())

        for i in range(0, len(content) - 5):
            self._trie.add_list_to_trie(content[i:i+6])

    def _generate_music(self):
        pass

    def start(self):
        """Käynnistää käyttöliittymän"""

        label = ttk.Label(master=self._root,
                          text="Musiikin generointi Markovin ketjun avulla")

        label.pack()

        open_button = ttk.Button(
            self._root,
            text="Avaa midi-tiedosto",
            command=self._select_file
        )
        open_button.pack(expand=False)

        generate_button = ttk.Button(
            self._root,
            text="Generoi musiikkia",
            command=self._generate_music
        )
        generate_button.pack(expand=False)

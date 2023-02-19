import os.path
import pygame
import tkinter as tk
import logging
import sys
from tkinter import ttk, Listbox, messagebox
from tkinter import filedialog as fd
from midi.midi import midi_to_string, string_to_midi
from trie.trie import Trie
from trie.generate_music import generate_music


logger = logging.getLogger(__name__)
logging.basicConfig(filename="debug.log", level=logging.DEBUG,
                    format="[%(asctime)s] %(levelname)s - %(message)s")


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
        try:
            file = fd.askopenfile(
                mode='r',
                filetypes=[('Midi-tiedostot', '*.midi'),
                           ('Midi-tiedostot', '*.mid'),
                           ('Midi-tiedostot', '*.MID'),
                           ('Midi-tiedostot', '*.MIDI')],
                initialdir="./data")
            if file == None:
                return
        except IOError:
            print("eerror: ", IOError)
            messagebox.showerror("Tiedostoa ei voitu avata",
                                 "Tiedosto ei ollut midi-tiedosto.")
            return

        try:
            self._content = list(midi_to_string(
                os.path.abspath(file.name)).split())
        except:
            messagebox.showerror("Tiedostoa ei voitu avata",
                                 "Tiedosto ei ollut midi-tiedosto.")
            return

        for i in range(2, 7):
            for j in range(0, len(self._content) - i):
                self._trie.add_list_to_trie(self._content[j:j+i])

        self._generate_button["state"] = tk.NORMAL

    def _generate_music(self):
        """Generoi musiikkia valitun prefix-pituuden mukaan
        """
        selected_lenght = self._select_prefix.curselection()
        if selected_lenght == None or len(selected_lenght) == 0:
            messagebox.showerror(
                "Prefixin pituutta ei valittu", "Valitse prefixin pituus.")
            return

        prefix_lenght = selected_lenght[0] + 1
        prefix = []

        for i in range(0, prefix_lenght):
            prefix.append(self._content[i])

        self._generated_music = prefix[:]

        while len(self._generated_music) < len(self._content) or self._generated_music[-1][:4] != self._content[-1][:4]:
            music, new_prefix = generate_music(
                self._trie, self._generated_music, prefix)
            self._generated_music = music[:]

            prefix = new_prefix[:]
            prefix.pop(0)

        generated_music_to_string = " ".join(self._generated_music)
        generated_music_to_midi = string_to_midi(generated_music_to_string)
        generated_music_to_midi.write("midi", "./data/generated.midi")

        self._play_midi_button["state"] = tk.NORMAL

    def _play_midi(self):
        """Soittaa generoidun musiikin
        """
        pygame.mixer.music.play()
        logger.info("music started")

        self._stop_music_button["state"] = tk.NORMAL

    def _stop_music(self):
        logger.debug("stop playing music")
        pygame.mixer.music.fadeout(1000)
        logger.info("music faded out")
        pygame.mixer.music.stop()
        logger.info("music stopped")
 #       pygame.mixer.music.unload()
        logger.info("music unloaded from mixer")

    def start(self):
        """Käynnistää käyttöliittymän"""

        freq = 44100
        bitsize = -16
        channels = 2
        buffer = 1024
        logger.debug("initialize mixer")
        pygame.mixer.init(freq, bitsize, channels, buffer)

        pygame.mixer.music.set_volume(0.8)
        logger.debug("start playing music")

        try:
            pygame.mixer.music.load("./data/generated.midi")
            logger.info("music load to mixer")
        except pygame.error:
            messagebox.showerror("Midin soittaminen ei onnistu",
                                 "Virhe midi-tiedoston toistamisessa")

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

        text = ttk.Label(
            text="Valitse kuinka monta nuottia generoinnissa käytetään")
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

        self._generate_button = ttk.Button(
            self._root,
            text="Generoi musiikkia",
            command=self._generate_music,
            state=tk.DISABLED
        )
        self._generate_button.pack(padx=5, pady=5, expand=False)

        self._play_midi_button = ttk.Button(
            self._root,
            text="Soita generoitu musiikki",
            state=tk.DISABLED,
            command=self._play_midi
        )
        self._play_midi_button.pack(padx=5, pady=5, expand=False)

        self._stop_music_button = ttk.Button(
            self._root,
            text="Pysäytä musiikin toisto",
            command=self._stop_music,
            state=tk.DISABLED
        )
        self._stop_music_button.pack(padx=5, pady=5, expand=False)

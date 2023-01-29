from tkinter import Tk, ttk, constants


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka"""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan

        Args:
            root: Tkinter-elemnetti, jonka sisään käyttöliittymä alustetaan
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän"""

        label = ttk.Label(master=self._root, text="Markovin ketju -säveltäjä")

        label.pack(side=constants.LEFT)
        





class Trie:
    """Luokka, joka kuvaa Prefix Tree -tietorakenteen
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden Trie-tietorakenteen"""
        self.root = TrieNode()

    def add_list_to_trie(self, note_list):
        """Lisää Trie-tietokantaan uuden tekstin

        Args:
            note_list: list of strings
                luettero lisättävistä nuoteista
        """
        nxt = self.root
        for i in note_list:
            nxt = nxt.add_note(i)
            nxt.freq += 1

    def search_given_prefix(self, list_of_notes):
        """Etsii Trie-tietokannasta tekstiä

        Args:
            string: str
                etsittävä teksti

        Returns:
            True, jos etsittävä prefix löytyy tietorakenteesta
            False, jos prefixiä ei löydy
        """
        nxt2 = self.root
        for i in list_of_notes:
            if i not in nxt2.nodes:
                return False
            nxt2 = nxt2.nodes[i]
        return True

    def return_choices(self, prefix):
        """Etsii nuottivaihtoehdot annetulle prefixille

        Args:
            prefix: list of strings
                luettelo nuoteista, joiden jälkeisiä vaihtoehtoja etsitään

        Returns:
            dictionary:
                dictionary, joka sisältää annetun prefixiä seuraavat nuottivaihtoehdot
        """
        nxt = self.root
        for i in prefix:
            if i not in nxt.nodes:
                return []

            nxt = nxt.nodes[i]
        return list(nxt.nodes.keys())

    def size(self, current=None):
        """Palauttaa Trie-tietorakenteen solmujen määrän

        Args:
            current:
                lähtösolmu, oletuksena Prefic puun juuri

        Returns:
            int:
                solmujen määrä
        """
        if not current:
            current = self.root
        count = 1
        for note in current.nodes:
            count += self.size(current.nodes[note])
        return count


class TrieNode:
    """Luokka, joka kuvaa Trie-tietorakenteen yksittäisen solmun
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden solmun
        """
        self.nodes = {}
        self.freq = 0

    def add_note(self, note):
        """Lisää merkin Trie-solmuun

        Args:
            note: str
                nuotti, joka lisätään Trie-solmuun

        Returns:
            dictionary, joka pitää kirjaa solmun kaikista alasolmuista
        """
        if note not in self.nodes:
            self.nodes[note] = TrieNode()
        return self.nodes[note]

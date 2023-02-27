
class Trie:
    """Luokka, joka kuvaa Prefix Tree -tietorakenteen
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden Trie-tietorakenteen"""
        self.root = _TrieNode()

    def add_list_to_trie(self, note_list):
        """Lisää Trie-tietokantaan uuden tekstin

        Args:
            note_list: list of strings
                luettero lisättävistä nuoteista
        """
        nxt = self.root
        for note in note_list:
            nxt = nxt.add_note(note)

    def search_given_prefix(self, list_of_notes):
        """Etsii Trie-tietokannasta tekstiä

        Args:
            list_of_notes: list of notes
                etsittävien nuottien luettelo

        Returns:
            True, jos etsittävä prefix löytyy tietorakenteesta
            False, jos prefixiä ei löydy
        """
        nxt2 = self.root
        for note in list_of_notes:
            if note not in nxt2.nodes:
                return False
            nxt2 = nxt2.nodes[note]
        return True

    def return_choices(self, prefix):
        """Etsii nuottivaihtoehdot annetulle prefixille

        Args:
            prefix: list of strings
                luettelo nuoteista, joiden jälkeisiä vaihtoehtoja etsitään

        Returns:
            dictionary:
                dictionary, jossa avaimina annettua prefixiä seuraavat nuottivaihtoehdot
                sekä arvoina nuottivaihtoehtojen esiintymismäärät
                jos prefixiä ei löydy, niin palautetaan tyhjä dictionary
        """
        nxt = self.root
        for note in prefix:
            if note not in nxt.nodes:
                return {}

            nxt = nxt.nodes[note]
        return nxt.freq

    def size(self, current=None):
        """Palauttaa Trie-tietorakenteen solmujen määrän

        Args:
            current:
                lähtösolmu, oletuksena Prefix-puun juuri

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


class _TrieNode:
    """Luokka, joka kuvaa Trie-tietorakenteen yksittäisen solmun
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden solmun
        """
        self.nodes = {}
        self.freq = {}

    def add_note(self, note):
        """Lisää merkin Trie-solmuun

        Args:
            note: str
                nuotti, joka lisätään Trie-solmuun

        Returns:
            dictionary, joka pitää kirjaa solmun kaikista alasolmuista ja niiden esiintyvyysmäärästä
        """
        if note not in self.nodes:
            self.nodes[note] = _TrieNode()
            self.freq[note] = 1
        else:
            self.freq[note] += 1
        return self.nodes[note]

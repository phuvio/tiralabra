import random


def generate_music(trie, generated_music, prefix):
    """Funktio, joka generoi annetuista tiedoista musiikkia

    Args:
        trie: trie-tietorakenne
            tietorakenne, johon on syötetty opetuksessa käytetty kappale
        generated_music: list of strings
            luettelo generoiduista nuoteista stringeinä
        prefix: list of strings
            luettelo nuoteista, jotka muodostavat etsinnässä käytetyn prefixin

    Returns:
        generated_music: list of strings
            luettelo generoiduista nuoteista stringeinä
        prefix: list of strings
            luettelo nuoteista, jotka muodostavat uuden prefixin
    """
    if trie.search_given_prefix(prefix):
        notes = list(trie.return_choices(prefix).keys())
        weights = list(trie.return_choices(prefix).values())

        next_note = random.choices(notes, weights)

        generated_music.append(next_note[0])
        prefix.append(next_note[0])

        return generated_music, prefix

    else:
        first_in_prefix = prefix.pop(0)

        new_prefix = prefix[:]
        music, prefix = generate_music(trie, generated_music, new_prefix)

        prefix.insert(0, first_in_prefix)
        generated_music = music[:]

        return generated_music, prefix

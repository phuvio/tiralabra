import unittest
from trie.trie import Trie
from trie.generate_music import generate_music


class TestGenerateMusic(unittest.TestCase):
    def setUp(self):
        self.test_trie = Trie()

        music = [
            'n_65_quarter',
            'n_38_half',
            'w_0.5',
            'n_62_eighth',
            'w_0.5',
            'n_65_quarter',
            'w_0.5'
        ]

        for i in range(2, 7):
            for j in range(0, len(music) - i):
                self.test_trie.add_list_to_trie(music[j:j+i])

    def test_generate_music_from_known_prefix(self):
        prefix = ['n_65_quarter', 'n_38_half', 'w_0.5',]
        new_music, new_prefix = generate_music(self.test_trie, [], prefix)

        self.assertEqual(new_music, ['n_62_eighth'])
        self.assertEqual(
            new_prefix, ['n_65_quarter', 'n_38_half', 'w_0.5', 'n_62_eighth'])

    def test_generate_music_from_unknown_prefix(self):
        prefix = ['n_70_quarter', 'n_28_half', 'w_1.5', 'n_62_eighth']
        new_music, new_prefix = generate_music(self.test_trie, [], prefix)

        self.assertEqual(new_music, ['w_0.5'])
        self.assertEqual(
            new_prefix, ['n_70_quarter', 'n_28_half', 'w_1.5', 'n_62_eighth', 'w_0.5'])

        prefix = ['n_28_quarter', 'w_2.5', 'n_65_quarter']
        new_music, new_prefix = generate_music(self.test_trie, [], prefix)

        self.assertEqual(new_music, ['n_38_half'])
        self.assertEqual(
            new_prefix, ['n_28_quarter', 'w_2.5', 'n_65_quarter', 'n_38_half'])

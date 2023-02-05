import unittest
from trie.trie import Trie, TrieNode


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.test_trie = Trie()

        self.list_of_notes = [
            'n_65_quarter',
            'n_38_half',
            'w_0.5',
            'n_62_eighth',
            'w_0.5',
            'n_65_quarter',
            'w_0.5']

        self.second_list_of_notes = [
            'n_65_quarter',
            'n_69_quarter',
            'n_67_eighth',
            'n_69_eighth']

        self.third_list_of_notes = [
            'n_62_quarter',
            'n_70_half',
            'n_38_half']

    def test_add_notes_to_trie(self):
        self.test_trie.add_list_to_trie(self.list_of_notes)

        self.assertEqual(self.test_trie.size(), 8)

    def test_add_same_list_to_trie(self):
        self.test_trie.add_list_to_trie(self.list_of_notes)
        self.test_trie.add_list_to_trie(self.list_of_notes)

        self.assertEqual(self.test_trie.size(), 8)

    def test_add_two_lists_with_first_same_note(self):
        self.test_trie.add_list_to_trie(self.list_of_notes)
        self.test_trie.add_list_to_trie(self.second_list_of_notes)

        self.assertEqual(self.test_trie.size(), 11)

    def test_add_two_lists_with_different_notes(self):
        self.test_trie.add_list_to_trie(self.list_of_notes)
        self.test_trie.add_list_to_trie(self.third_list_of_notes)

        self.assertEqual(self.test_trie.size(), 11)

    def test_find_given_prefix(self):
        self.test_trie.add_list_to_trie(self.list_of_notes)
        self.test_trie.add_list_to_trie(self.second_list_of_notes)

        found_prefix = self.test_trie.search_given_prefix([
            'n_65_quarter',
            'n_69_quarter',
            'n_67_eighth',
            'n_69_eighth'])

        self.assertEqual(found_prefix, True)

    def test_find_given_prefix_not_found(self):
        self.test_trie.add_list_to_trie(self.list_of_notes)
        self.test_trie.add_list_to_trie(self.second_list_of_notes)

        found_prefix = self.test_trie.search_given_prefix([
            'n_65_quarter',
            'n_69_quarter',
            'n_75_eighth',
            'n_69_eighth'])

        self.assertEqual(found_prefix, False)

    def test_possible_choices_from_given_prefix(self):
        self.test_trie.add_list_to_trie(self.second_list_of_notes)
        self.test_trie.add_list_to_trie([
            'n_65_quarter',
            'n_69_quarter',
            'n_67_eighth',
            'n_65_eighth'])
        self.test_trie.add_list_to_trie([
            'n_65_quarter',
            'n_69_quarter',
            'n_67_eighth',
            'n_70_eighth'])

        found_choices = self.test_trie.return_choices([
            'n_65_quarter',
            'n_69_quarter',
            'n_67_eighth'])

        self.assertEqual(
            found_choices, ['n_69_eighth', 'n_65_eighth', 'n_70_eighth'])

    def test_no_found_choices_from_given_prefix(self):
        self.test_trie.add_list_to_trie(self.third_list_of_notes)

        found_choices = self.test_trie.return_choices([
            'n_62_quarter',
            'n_70_half',
            'n_38_half'])

        self.assertEqual(found_choices, [])

    def test_prefix_not_found(self):
        self.test_trie.add_list_to_trie(self.third_list_of_notes)

        found_choices = self.test_trie.return_choices([
            'n_50_quarter'
        ])

        self.assertEqual(found_choices, [])
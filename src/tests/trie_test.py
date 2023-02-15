import unittest
from trie.trie import Trie
from midi.midi import midi_to_string


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

        ode_to_joy = midi_to_string("./src/tests/ode_to_joy.midi")
        self.ode_to_joy = ode_to_joy.split()

    def test_add_notes_to_trie(self):
        self.test_trie.add_list_to_trie(self.list_of_notes)

        self.assertEqual(self.test_trie.size(), 8)

    def test_add_ode_to_joy_to_trie(self):
        for i in range(2, 7):
            for j in range(0, len(self.ode_to_joy) - i):
                self.test_trie.add_list_to_trie(self.ode_to_joy[j:j+i])

        self.assertEqual(self.test_trie.size(), 263)

    def test_add_same_list_to_trie(self):
        self.test_trie.add_list_to_trie(self.list_of_notes)
        self.test_trie.add_list_to_trie(self.list_of_notes)

        self.assertEqual(self.test_trie.size(), 8)

    def test_add_ode_to_joy_twice_to_trie(self):
        for i in range(2, 7):
            for j in range(0, len(self.ode_to_joy) - i):
                self.test_trie.add_list_to_trie(self.ode_to_joy[j:j+i])

        for i in range(2, 7):
            for j in range(0, len(self.ode_to_joy) - i):
                self.test_trie.add_list_to_trie(self.ode_to_joy[j:j+i])

        self.assertEqual(self.test_trie.size(), 263)

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

    def test_given_prefix_not_found(self):
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
            list(found_choices.keys()), ['n_69_eighth', 'n_65_eighth', 'n_70_eighth'])

    def test_possible_choices_from_given_prefix_with_more_probabilities(self):
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
            list(found_choices.keys()), ['n_69_eighth', 'n_65_eighth', 'n_70_eighth'])
        self.assertEqual(
            found_choices['n_69_eighth'], 1
        )
        self.assertEqual(
            found_choices['n_65_eighth'], 2
        )
        self.assertEqual(
            found_choices['n_70_eighth'], 2
        )

    def test_no_found_choices_from_given_prefix(self):
        self.test_trie.add_list_to_trie(self.third_list_of_notes)

        found_choices = self.test_trie.return_choices([
            'n_62_quarter',
            'n_70_half',
            'n_38_half'])

        self.assertEqual(found_choices, {})

    def test_prefix_not_found(self):
        self.test_trie.add_list_to_trie(self.third_list_of_notes)

        found_choices = self.test_trie.return_choices([
            'n_50_quarter'
        ])

        self.assertEqual(found_choices, {})

    def test_find_given_prefixes_from_ode_to_joy(self):
        for i in range(2, 7):
            for j in range(0, len(self.ode_to_joy) - i):
                self.test_trie.add_list_to_trie(self.ode_to_joy[j:j+i])
        
        prefixes = [
            [],
            ['n_48_eighth'],
            ['n_48_quarter',],
            ['n_48_half'],
            ['n_50_eighth'],
            ['n_50_quarter'],
            ['n_50_half'],
            ['n_52_eighth'],
            ['n_52_quarter'],
            ['n_53_eighth'],
            ['n_53_quarter'],
            ['n_55_quarter'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.5'],
            ['w_2.0'],
            ['n_48_eighth','w_0.5',],
            ['n_48_quarter','w_1.0',],
            ['n_48_quarter','w_2.0',],
            ['n_50_eighth','w_0.5',],
            ['n_50_half','w_2.0',],
            ['n_50_quarter','w_1.0',],
            ['n_50_quarter','w_1.5',],
            ['n_50_quarter','w_2.0',],
            ['n_52_eighth','w_0.5',],
            ['n_52_quarter','w_1.0',],
            ['n_52_quarter','w_1.5',],
            ['n_53_eighth','w_0.5',],
            ['n_53_quarter','w_1.0',],
            ['n_55_quarter','w_1.0',],
            ['w_0.5','n_48_quarter',],
            ['w_0.5','n_50_half',],
            ['w_0.5','n_52_quarter',],
            ['w_0.5','n_53_eighth',],
            ['w_1.0','n_48_quarter',],
            ['w_1.0','n_50_quarter',],
            ['w_1.0','n_52_eighth',],
            ['w_1.0','n_52_quarter',],
            ['w_1.0','n_53_quarter',],
            ['w_1.0','n_55_quarter',],
            ['w_1.5','n_48_eighth',],
            ['w_1.5','n_50_eighth',],
            ['w_2.0','n_50_quarter',],
            ['w_2.0','n_52_quarter',],
            ['n_48_eighth','w_0.5','n_48_quarter',],
            ['n_48_quarter','w_1.0','n_48_quarter',],
            ['n_48_quarter','w_1.0','n_50_quarter',],
            ['n_48_quarter','w_2.0','n_50_quarter',],
            ['n_50_eighth','w_0.5','n_50_half',],
            ['n_50_half','w_2.0','n_52_quarter',],
            ['n_50_quarter','w_1.0','n_48_quarter',],
            ['n_50_quarter','w_1.0','n_50_quarter',],
            ['n_50_quarter','w_1.0','n_52_eighth',],
            ['n_50_quarter','w_1.0','n_52_quarter',],
            ['n_50_quarter','w_1.5','n_48_eighth',],
            ['n_50_quarter','w_2.0','n_52_quarter',],
            ['n_52_eighth','w_0.5','n_53_eighth',],
            ['n_52_quarter','w_1.0','n_48_quarter',],
            ['n_52_quarter','w_1.0','n_50_quarter',],
            ['n_52_quarter','w_1.0','n_52_quarter',],
            ['n_52_quarter','w_1.0','n_53_quarter',],
            ['n_52_quarter','w_1.5','n_50_eighth',],
            ['n_53_eighth','w_0.5','n_52_quarter',],
            ['n_53_quarter','w_1.0','n_52_quarter',],
            ['n_53_quarter','w_1.0','n_55_quarter',],
            ['n_55_quarter','w_1.0','n_53_quarter',],
            ['n_55_quarter','w_1.0','n_55_quarter',],
            ['w_0.5','n_48_quarter','w_2.0',],
            ['w_0.5','n_50_half','w_2.0',],
            ['w_0.5','n_52_quarter','w_1.0',],
            ['w_0.5','n_53_eighth','w_0.5',],
            ['w_1.0','n_48_quarter','w_1.0',],
            ['w_1.0','n_50_quarter','w_1.0',],
            ['w_1.0','n_50_quarter','w_1.5',],
            ['w_1.0','n_50_quarter','w_2.0',],
            ['w_1.0','n_52_eighth','w_0.5',],
            ['w_1.0','n_52_quarter','w_1.0',],
            ['w_1.0','n_52_quarter','w_1.5',],
            ['w_1.0','n_53_quarter','w_1.0',],
            ['w_1.0','n_55_quarter','w_1.0',],
            ['w_1.5','n_48_eighth','w_0.5',],
            ['w_1.5','n_50_eighth','w_0.5',],
            ['w_2.0','n_50_quarter','w_1.0',],
            ['w_2.0','n_52_quarter','w_1.0',],
            ['n_48_eighth','w_0.5','n_48_quarter','w_2.0',],
            ['n_48_quarter','w_1.0','n_48_quarter','w_1.0',],
            ['n_48_quarter','w_1.0','n_50_quarter','w_1.0',],
            ['n_48_quarter','w_1.0','n_50_quarter','w_2.0',],
            ['n_48_quarter','w_2.0','n_50_quarter','w_1.0',],
            ['n_50_eighth','w_0.5','n_50_half','w_2.0',],
            ['n_50_half','w_2.0','n_52_quarter','w_1.0',],
            ['n_50_quarter','w_1.0','n_48_quarter','w_1.0',],
            ['n_50_quarter','w_1.0','n_50_quarter','w_1.0',],
            ['n_50_quarter','w_1.0','n_52_eighth','w_0.5',],
            ['n_50_quarter','w_1.0','n_52_quarter','w_1.0',],
            ['n_50_quarter','w_1.5','n_48_eighth','w_0.5',],
            ['n_50_quarter','w_2.0','n_52_quarter','w_1.0',],
            ['n_52_eighth','w_0.5','n_53_eighth','w_0.5',],
            ['n_52_quarter','w_1.0','n_48_quarter','w_1.0',],
            ['n_52_quarter','w_1.0','n_50_quarter','w_1.0',],
            ['n_52_quarter','w_1.0','n_50_quarter','w_1.5',],
            ['n_52_quarter','w_1.0','n_52_quarter','w_1.0',],
            ['n_52_quarter','w_1.0','n_52_quarter','w_1.5',],
            ['n_52_quarter','w_1.0','n_53_quarter','w_1.0',],
            ['n_52_quarter','w_1.5','n_50_eighth','w_0.5',],
            ['n_53_eighth','w_0.5','n_52_quarter','w_1.0',],
            ['n_53_quarter','w_1.0','n_52_quarter','w_1.0',],
            ['n_53_quarter','w_1.0','n_55_quarter','w_1.0',],
            ['n_55_quarter','w_1.0','n_53_quarter','w_1.0',],
            ['n_55_quarter','w_1.0','n_55_quarter','w_1.0',],
            ['w_0.5','n_48_quarter','w_2.0','n_50_quarter',],
            ['w_0.5','n_50_half','w_2.0','n_52_quarter',],
            ['w_0.5','n_52_quarter','w_1.0','n_48_quarter',],
            ['w_0.5','n_52_quarter','w_1.0','n_50_quarter',],
            ['w_0.5','n_53_eighth','w_0.5','n_52_quarter',],
            ['w_1.0','n_48_quarter','w_1.0','n_48_quarter',],
            ['w_1.0','n_48_quarter','w_1.0','n_50_quarter',],
            ['w_1.0','n_50_quarter','w_1.0','n_48_quarter',],
            ['w_1.0','n_50_quarter','w_1.0','n_52_eighth',],
            ['w_1.0','n_50_quarter','w_1.0','n_52_quarter',],
            ['w_1.0','n_50_quarter','w_1.5','n_48_eighth',],
            ['w_1.0','n_50_quarter','w_2.0','n_52_quarter',],
            ['w_1.0','n_52_eighth','w_0.5','n_53_eighth',],
            ['w_1.0','n_52_quarter','w_1.0','n_48_quarter',],
            ['w_1.0','n_52_quarter','w_1.0','n_50_quarter',],
            ['w_1.0','n_52_quarter','w_1.0','n_52_quarter',],
            ['w_1.0','n_52_quarter','w_1.0','n_53_quarter',],
            ['w_1.0','n_52_quarter','w_1.5','n_50_eighth',],
            ['w_1.0','n_53_quarter','w_1.0','n_52_quarter',],
            ['w_1.0','n_53_quarter','w_1.0','n_55_quarter',],
            ['w_1.0','n_55_quarter','w_1.0','n_53_quarter',],
            ['w_1.0','n_55_quarter','w_1.0','n_55_quarter',],
            ['w_1.5','n_48_eighth','w_0.5','n_48_quarter',],
            ['w_1.5','n_50_eighth','w_0.5','n_50_half',],
            ['w_2.0','n_50_quarter','w_1.0','n_50_quarter',],
            ['w_2.0','n_52_quarter','w_1.0','n_52_quarter',],
            ['n_48_eighth','w_0.5','n_48_quarter','w_2.0','n_50_quarter',],
            ['n_48_quarter','w_1.0','n_48_quarter','w_1.0','n_50_quarter',],
            ['n_48_quarter','w_1.0','n_50_quarter','w_1.0','n_52_eighth',],
            ['n_48_quarter','w_1.0','n_50_quarter','w_1.0','n_52_quarter',],
            ['n_48_quarter','w_2.0','n_50_quarter','w_1.0','n_50_quarter',],
            ['n_50_eighth','w_0.5','n_50_half','w_2.0','n_52_quarter',],
            ['n_50_half','w_2.0','n_52_quarter','w_1.0','n_52_quarter',],
            ['n_50_quarter','w_1.0','n_48_quarter','w_1.0','n_48_quarter',],
            ['n_50_quarter','w_1.0','n_48_quarter','w_1.0','n_50_quarter',],
            ['n_50_quarter','w_1.0','n_50_quarter','w_1.0','n_52_quarter',],
            ['n_50_quarter','w_1.0','n_52_eighth','w_0.5','n_53_eighth',],
            ['n_50_quarter','w_1.0','n_52_quarter','w_1.0','n_48_quarter',],
            ['n_50_quarter','w_1.0','n_52_quarter','w_1.0','n_50_quarter',],
            ['n_50_quarter','w_1.0','n_52_quarter','w_1.0','n_52_quarter',],
            ['n_50_quarter','w_1.5','n_48_eighth','w_0.5','n_48_quarter',],
            ['n_50_quarter','w_2.0','n_52_quarter','w_1.0','n_52_quarter',],
            ['n_52_eighth','w_0.5','n_53_eighth','w_0.5','n_52_quarter',],
            ['n_52_quarter','w_1.0','n_48_quarter','w_1.0','n_50_quarter',],
            ['n_52_quarter','w_1.0','n_50_quarter','w_1.0','n_48_quarter',],
            ['n_52_quarter','w_1.0','n_50_quarter','w_1.5','n_48_eighth',],
            ['n_52_quarter','w_1.0','n_52_quarter','w_1.0','n_52_quarter',],
            ['n_52_quarter','w_1.0','n_52_quarter','w_1.0','n_53_quarter',],
            ['n_52_quarter','w_1.0','n_52_quarter','w_1.5','n_50_eighth',],
            ['n_52_quarter','w_1.0','n_53_quarter','w_1.0','n_55_quarter',],
            ['n_52_quarter','w_1.5','n_50_eighth','w_0.5','n_50_half',],
            ['n_53_eighth','w_0.5','n_52_quarter','w_1.0','n_48_quarter',],
            ['n_53_eighth','w_0.5','n_52_quarter','w_1.0','n_50_quarter',],
            ['n_53_quarter','w_1.0','n_52_quarter','w_1.0','n_50_quarter',],
            ['n_53_quarter','w_1.0','n_55_quarter','w_1.0','n_55_quarter',],
            ['n_55_quarter','w_1.0','n_53_quarter','w_1.0','n_52_quarter',],
            ['n_55_quarter','w_1.0','n_55_quarter','w_1.0','n_53_quarter',],
            ['w_0.5','n_48_quarter','w_2.0','n_50_quarter','w_1.0',],
            ['w_0.5','n_50_half','w_2.0','n_52_quarter','w_1.0',],
            ['w_0.5','n_52_quarter','w_1.0','n_48_quarter','w_1.0',],
            ['w_0.5','n_52_quarter','w_1.0','n_50_quarter','w_1.0',],
            ['w_0.5','n_53_eighth','w_0.5','n_52_quarter','w_1.0',],
            ['w_1.0','n_48_quarter','w_1.0','n_48_quarter','w_1.0',],
            ['w_1.0','n_48_quarter','w_1.0','n_50_quarter','w_1.0',],
            ['w_1.0','n_48_quarter','w_1.0','n_50_quarter','w_2.0',],
            ['w_1.0','n_50_quarter','w_1.0','n_48_quarter','w_1.0',],
            ['w_1.0','n_50_quarter','w_1.0','n_52_eighth','w_0.5',],
            ['w_1.0','n_50_quarter','w_1.0','n_52_quarter','w_1.0',],
            ['w_1.0','n_50_quarter','w_1.5','n_48_eighth','w_0.5',],
            ['w_1.0','n_50_quarter','w_2.0','n_52_quarter','w_1.0',],
            ['w_1.0','n_52_eighth','w_0.5','n_53_eighth','w_0.5',],
            ['w_1.0','n_52_quarter','w_1.0','n_48_quarter','w_1.0',],
            ['w_1.0','n_52_quarter','w_1.0','n_50_quarter','w_1.0',],
            ['w_1.0','n_52_quarter','w_1.0','n_50_quarter','w_1.5',],
            ['w_1.0','n_52_quarter','w_1.0','n_52_quarter','w_1.0',],
            ['w_1.0','n_52_quarter','w_1.0','n_52_quarter','w_1.5',],
            ['w_1.0','n_52_quarter','w_1.0','n_53_quarter','w_1.0',],
            ['w_1.0','n_52_quarter','w_1.5','n_50_eighth','w_0.5',],
            ['w_1.0','n_53_quarter','w_1.0','n_52_quarter','w_1.0',],
            ['w_1.0','n_53_quarter','w_1.0','n_55_quarter','w_1.0',],
            ['w_1.0','n_55_quarter','w_1.0','n_53_quarter','w_1.0',],
            ['w_1.0','n_55_quarter','w_1.0','n_55_quarter','w_1.0',],
            ['w_1.5','n_48_eighth','w_0.5','n_48_quarter','w_2.0',],
            ['w_1.5','n_50_eighth','w_0.5','n_50_half','w_2.0',],
            ['w_2.0','n_50_quarter','w_1.0','n_50_quarter','w_1.0',],
            ['w_2.0','n_52_quarter','w_1.0','n_52_quarter','w_1.0',],
        ]

        found_keys = [
            ['n_48_eighth', 'n_48_quarter', 'n_50_eighth', 'n_50_half',
            'n_50_quarter', 'n_52_eighth', 'n_52_quarter', 'n_53_eighth',
            'n_53_quarter', 'n_55_quarter', 'w_0.5', 'w_1.0', 'w_1.5', 'w_2.0'],
            ['w_0.5'],
            ['w_1.0','w_2.0'],
            [],
            ['w_0.5'],
            ['w_1.0','w_1.5','w_2.0'],
            ['w_2.0'],
            ['w_0.5'],
            ['w_1.0','w_1.5'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0'],
            ['n_48_quarter', 'n_50_half', 'n_52_quarter', 'n_53_eighth'],
            ['n_48_quarter', 'n_50_quarter', 'n_52_eighth', 'n_52_quarter',
            'n_53_quarter', 'n_55_quarter'],
            ['n_48_eighth', 'n_50_eighth'],
            ['n_50_quarter', 'n_52_quarter'],
            ['n_48_quarter'],
            ['n_48_quarter', 'n_50_quarter'],
            ['n_50_quarter'],
            ['n_50_half'],
            ['n_52_quarter'],
            ['n_48_quarter', 'n_50_quarter', 'n_52_eighth', 'n_52_quarter'],
            ['n_48_eighth',],
            ['n_52_quarter'],
            ['n_53_eighth'],
            ['n_48_quarter', 'n_50_quarter', 'n_52_quarter', 'n_53_quarter',],
            ['n_50_eighth',],
            ['n_52_quarter',],
            ['n_52_quarter', 'n_55_quarter'],
            ['n_53_quarter', 'n_55_quarter'],
            ['w_2.0'],
            ['w_2.0'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0', 'w_1.5', 'w_2.0'],
            ['w_0.5'],
            ['w_1.0', 'w_1.5'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_2.0'],
            ['w_1.0'],
            ['w_1.0', 'w_2.0'],
            ['w_1.0'],
            ['w_2.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0', 'w_1.5'],
            ['w_1.0', 'w_1.5'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['n_50_quarter'],
            ['n_52_quarter'],
            ['n_48_quarter', 'n_50_quarter'],
            ['n_52_quarter'],
            ['n_48_quarter', 'n_50_quarter'],
            ['n_48_quarter', 'n_52_eighth', 'n_52_quarter'],
            ['n_48_eighth'],
            ['n_52_quarter'],
            ['n_53_eighth'],
            ['n_48_quarter', 'n_50_quarter', 'n_52_quarter', 'n_53_quarter'],
            ['n_50_eighth'],
            ['n_52_quarter', 'n_55_quarter'],
            ['n_53_quarter', 'n_55_quarter'],
            ['n_48_quarter'],
            ['n_50_half'],
            ['n_50_quarter'],
            ['n_52_quarter'],
            ['n_50_quarter'],
            ['n_50_quarter'],
            ['n_52_eighth', 'n_52_quarter'],
            ['n_52_quarter'],
            ['n_50_quarter'],
            ['n_52_quarter'],
            ['n_52_quarter'],
            ['n_48_quarter', 'n_50_quarter'],
            ['n_52_quarter'],
            ['n_53_eighth'],
            ['n_48_quarter', 'n_50_quarter', 'n_52_quarter'],
            ['n_48_quarter'],
            ['n_52_quarter'],
            ['n_52_quarter'],
            ['n_50_quarter'],
            ['n_48_quarter'],
            ['n_48_eighth'],
            ['n_52_quarter', 'n_53_quarter'],
            ['n_50_eighth'],
            ['n_55_quarter'],
            ['n_50_half'],
            ['n_48_quarter', 'n_50_quarter'],
            ['n_50_quarter'],
            ['n_55_quarter'],
            ['n_52_quarter'],
            ['n_53_quarter'],    
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0', 'w_2.0'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0', 'w_1.5'],
            ['w_1.0', 'w_1.5'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_2.0'],
            ['w_2.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_2.0'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.5'],
            ['w_1.5'],
            ['w_2.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_0.5'],
            ['w_1.0'],
            ['w_2.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['w_1.0'],
            ['n_50_quarter'],
            ['n_52_quarter'],
            ['n_50_quarter'],
            ['n_48_quarter'],
            ['n_48_quarter','n_50_quarter'],
            ['n_50_quarter'],
            ['n_52_eighth', 'n_52_quarter'],
            ['n_52_quarter'],
            ['n_48_quarter', 'n_50_quarter'],
            ['n_53_eighth'],
            ['n_48_quarter', 'n_50_quarter', 'n_52_quarter'],
            ['n_48_quarter'],
            ['n_52_quarter'],
            ['n_52_quarter'],
            ['n_50_quarter'],
            ['n_48_quarter'],
            ['n_48_eighth'],
            ['n_53_quarter'],
            ['n_50_eighth'],
            ['n_55_quarter'],
            ['n_50_half'],
            ['n_50_quarter'],
            ['n_55_quarter'],
            ['n_52_quarter'],
            ['n_53_quarter'],
            ['n_50_quarter'],
            ['n_52_quarter'],
            ['n_52_quarter'],
            ['n_52_quarter', 'n_53_quarter'],
        ]

        found_weights = [
            [85,239,30,30,68,50,12,5,30,5,15,6,10,10],
            [6],
            [45,5],
            [],
            [5],
            [55,8,5],
            [5],
            [10],
            [80,5],
            [10],
            [30],
            [30],
            [5,5,10,10,],
            [60,30,30,64,45,10],
            [5,7],
            [10,5],
            [4],
            [12,24],
            [4],
            [4],
            [4],
            [16,16,4,8],
            [6],
            [4],
            [8],
            [20,12,24,8],
            [4],
            [8],
            [12,12],
            [12,12],
            [4],
            [4],
            [8],
            [8],
            [36],
            [40,7,4],
            [8],
            [44,4],
            [24],
            [24],
            [5],
            [4],
            [4],
            [8],
            [3],
            [9],
            [15,3],
            [3],
            [3],
            [3],
            [12],
            [3],
            [6],
            [12],
            [4],
            [3],
            [6],
            [6],
            [12,6],
            [12,3],
            [9],
            [3],
            [6],
            [9],
            [9],
            [9],
            [9],
            [3],
            [3],
            [3,3],
            [6],
            [9,18],
            [12,12,6],
            [5],
            [3],
            [6],
            [9,15,6,3],
            [3],
            [9,9],
            [9,9],
            [3],
            [3],
            [3],
            [6],
            [2],
            [6],
            [6,4],
            [2],
            [2],
            [2],
            [2],
            [6,2],
            [2],
            [4],
            [2,4,2],
            [2],
            [2],
            [4],
            [4],
            [8],
            [4],
            [6,2],
            [2],
            [6],
            [2],
            [2,2],
            [6],
            [6],
            [6],
            [6],
            [2],
            [2],
            [2],
            [2],
            [4],
            [6],
            [10,2],
            [8],
            [4],
            [8],
            [3],
            [2],
            [4],
            [2],
            [6,4],
            [2,2],
            [6],
            [2],
            [6],
            [6],
            [6],
            [6],
            [2],
            [2],
            [2],
            [4],
            [1],
            [3],
            [2],
            [3],
            [1],
            [1],
            [1],
            [3],
            [1],
            [1],
            [2],
            [1],
            [2],
            [1],
            [1],
            [1],
            [2],
            [2],
            [4],
            [2],
            [1],
            [3],
            [1],
            [3],
            [1],
            [1],
            [1],
            [3],
            [3],
            [3],
            [3],
            [1],
            [1],
            [1],
            [1],
            [1,1],
            [3],
            [3,2],
            [1],
            [3,1],
            [2],
            [1,2,1],
            [1],
            [1],
            [2],
            [1],
            [3],
            [2],
            [1],
            [1],
            [3],
            [1],
            [3],
            [3],
            [3],
            [3],
            [1],
            [1],
            [1],
            [1,1],
        ]

        for i in range(0, len(prefixes)):
            found_choices = self.test_trie.return_choices(prefixes[i])
            print(found_choices)
            keys = list(found_choices.keys())
            print(prefixes[i])
            print(sorted(keys))

            self.assertEqual(sorted(keys), found_keys[i])
            for j in range(0, len(keys)):
                print(found_choices[keys[j]])
                self.assertEqual(found_choices[keys[j]], found_weights[i][j])
        
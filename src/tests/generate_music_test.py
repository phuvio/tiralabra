import unittest
import random
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
        """
        testataan generoiko funktio oikean nuotin, kun prefix löytyy triestä ja sillä on vain yksi vaihtoehto
        """
        prefix = ['n_65_quarter', 'n_38_half', 'w_0.5',]
        new_music, new_prefix = generate_music(self.test_trie, [], prefix)

        self.assertEqual(new_music, ['n_62_eighth'])
        self.assertEqual(
            new_prefix, ['n_65_quarter', 'n_38_half', 'w_0.5', 'n_62_eighth'])

    def test_generate_music_from_unknown_prefix(self):
        """
        testataan generoiko funktio oikean nuotin, kun ainoastaan prefixin viimeinen nuotti löytyy triestä
        tämä testi ajetaan varmuuden vuoksi kahteen kertaan samalla trie-tietorakenteella
        """
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

    def test_generate_music_gives_correct_note(self):
        """
        sekoitetaan tuhat nuottia sisältävä luettelo ja tallennetaan se Trie-tietorakenteeseen
        arvotaan prefixin pituus ja valitaan siihen arpomalla nuotit edellä mainitusta sekoitetusta nuottiluettelosta
        tarkistetaan, että edellisessä kohdassa arvotulla prefixillä generoitu nuotti on mahdollinen
        toistetaan testi 10 000 kertaa
        """
        thousand_notes = ['w_1.0', 'n_65_quarter', 'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5',
                          'n_65_quarter', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_eighth', 'n_69_quarter',
                          'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_eighth', 'n_62_quarter', 'w_0.5',
                          'n_62_eighth', 'n_36_eighth', 'w_0.5', 'n_70_half', 'n_38_half', 'w_0.5',
                          'n_62_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5',
                          'n_65_quarter', 'n_70_quarter', 'w_1.0', 'n_62_quarter', 'n_65_quarter',
                          'w_0.5', 'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half', 'w_0.5',
                          'n_60_eighth', 'w_0.5', 'n_64_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5',
                          'n_60_quarter', 'n_67_quarter', 'w_1.0', 'n_72_quarter', 'n_60_quarter',
                          'w_0.5', 'n_40_eighth', 'w_0.5', 'n_69_half', 'n_41_half', 'w_0.5',
                          'n_60_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5',
                          'n_69_quarter', 'w_1.0', 'n_60_quarter', 'n_69_quarter', 'w_0.5', 'n_41_eighth',
                          'w_0.5', 'n_42_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_66_eighth',
                          'w_0.5', 'n_62_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_72_eighth',
                          'w_0.5', 'n_70_eighth', 'n_70_eighth', 'w_0.5', 'n_72_eighth', 'n_69_eighth',
                          'w_0.5', 'n_69_eighth', 'n_66_eighth', 'n_42_eighth', 'w_0.5', 'n_70_quarter',
                          'n_43_half', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5',
                          'n_62_quarter',
                          'n_70_eighth', 'w_0.5', 'n_72_eighth', 'w_0.5', 'n_70_16th', 'n_72_16th',
                          'w_0.25', 'n_70_16th', 'w_0.25', 'n_67_quarter', 'n_69_eighth', 'w_0.5',
                          'n_62_eighth', 'n_43_eighth', 'w_0.5', 'n_65_quarter', 'n_44_half',
                          'w_0.5', 'n_65_quarter', 'w_0.5', 'n_59_eighth', 'w_0.5', 'n_62_eighth',
                          'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'n_59_eighth', 'w_0.25',
                          'n_68_16th', 'w_0.25', 'n_67_eighth', 'n_68_eighth', 'w_0.5', 'n_65_eighth',
                          'n_65_eighth', 'n_44_eighth', 'w_0.5', 'n_65_quarter', 'n_62_quarter',
                          'n_45_quarter', 'w_1.0', 'n_33_quarter', 'w_0.5', 'n_65_16th', 'n_62_16th',
                          'w_0.25', 'n_67_16th', 'n_64_16th', 'w_0.25', 'n_64_quarter', 'n_61_quarter',
                          'w_2.0', 'n_41_16th', 'n_64_quarter', 'n_61_quarter', 'w_0.25', 'n_40_16th',
                          'w_0.25', 'n_38_16th', 'w_0.25', 'n_37_16th', 'w_0.25', 'n_65_quarter',
                          'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_quarter', 'w_0.5',
                          'n_67_eighth', 'w_0.5', 'n_65_eighth', 'n_69_quarter', 'w_0.5', 'n_67_eighth',
                          'w_0.5', 'n_69_eighth', 'n_62_quarter', 'w_0.5', 'n_62_eighth', 'n_36_eighth',
                          'w_0.5', 'n_70_half', 'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_eighth',
                          'w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_quarter', 'n_70_quarter',
                          'w_1.0', 'n_62_quarter',
                          'n_65_quarter', 'w_0.5', 'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half',
                          'w_0.5', 'n_60_eighth', 'w_0.5', 'n_64_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5',
                          'n_60_quarter', 'n_67_quarter', 'w_1.0', 'n_72_quarter', 'n_60_quarter', 'w_0.5',
                          'n_40_eighth', 'w_0.5', 'n_69_half', 'n_41_half', 'w_0.5', 'n_60_eighth', 'w_0.5',
                          'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_quarter', 'w_1.0',
                          'n_60_quarter', 'n_69_quarter', 'w_0.5', 'n_41_eighth', 'w_0.5', 'n_42_half',
                          'w_0.5', 'n_62_eighth', 'w_0.5', 'n_66_eighth', 'w_0.5',
                          'n_62_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_72_eighth', 'w_0.5',
                          'n_70_eighth', 'n_70_eighth', 'w_0.5', 'n_72_eighth', 'n_69_eighth', 'w_0.5',
                          'n_69_eighth', 'n_66_eighth', 'n_42_eighth', 'w_0.5', 'n_70_quarter', 'n_43_half',
                          'w_0.5', 'n_67_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_62_quarter',
                          'n_70_eighth', 'w_0.5', 'n_72_eighth', 'w_0.5', 'n_70_16th', 'n_72_16th',
                          'w_0.25', 'n_70_16th', 'w_0.25', 'n_67_quarter', 'n_69_eighth', 'w_0.5',
                          'n_62_eighth', 'n_43_eighth', 'w_0.5', 'n_65_quarter', 'n_44_half',
                          'w_0.5', 'n_65_quarter', 'w_0.5', 'n_59_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5',
                          'n_65_eighth', 'w_0.5', 'n_67_eighth', 'n_59_eighth', 'w_0.25', 'n_68_16th',
                          'w_0.25', 'n_67_eighth', 'n_68_eighth', 'w_0.5', 'n_65_eighth', 'n_65_eighth',
                          'n_44_eighth', 'w_0.5', 'n_65_quarter', 'n_62_quarter', 'n_45_quarter',
                          'w_1.0', 'n_33_quarter', 'w_0.5', 'n_65_16th', 'n_62_16th', 'w_0.25',
                          'n_67_16th', 'n_64_16th', 'w_0.25', 'n_64_quarter', 'n_61_quarter', 'w_2.0',
                          'n_41_16th', 'n_64_quarter', 'n_61_quarter', 'w_0.25', 'n_40_16th',
                          'w_0.25', 'n_38_16th', 'w_0.25', 'n_37_16th', 'w_0.25', 'n_76_eighth',
                          'n_35_quarter', 'w_0.5', 'n_77_eighth', 'n_74_16th', 'w_0.25', 'n_76_16th',
                          'w_0.25', 'n_77_eighth', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_79_16th',
                          'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_76_quarter', 'n_35_quarter',
                          'w_0.5', 'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_77_16th', 'n_76_eighth',
                          'w_0.25', 'n_76_eighth', 'w_0.25', 'n_74_16th', 'w_0.25',
                          'n_76_16th', 'w_0.25', 'n_76_eighth', 'n_35_quarter', 'w_0.5', 'n_77_eighth',
                          'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_77_eighth',
                          'w_0.25', 'n_76_16th', 'w_0.25', 'n_79_16th', 'n_74_16th', 'w_0.25',
                          'n_76_16th', 'w_0.25', 'n_81_eighth',
                          'n_35_quarter', 'w_0.5', 'n_79_16th', 'n_74_16th', 'n_81_16th',
                          'w_0.25', 'n_79_16th', 'n_76_16th', 'w_0.25', 'n_77_eighth', 'n_77_eighth',
                          'w_0.25', 'n_76_16th', 'w_0.25', 'n_76_16th', 'n_74_16th', 'w_0.25', 'n_76_16th',
                          'w_0.25', 'n_74_quarter', 'n_33_quarter', 'w_0.5', 'n_72_16th',
                          'w_0.25', 'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_74_16th',
                          'w_0.25', 'n_72_16th', 'n_72_quarter', 'w_0.25', 'n_74_16th',
                          'w_0.25', 'n_33_quarter',
                          'w_0.5', 'n_72_eighth', 'w_0.25', 'n_74_16th', 'w_0.25',
                          'n_76_16th', 'n_72_eighth', 'w_0.25', 'n_74_16th', 'w_0.25', 'n_72_16th',
                          'w_0.25', 'n_74_16th', 'w_0.25', 'n_72_16th', 'n_69_16th', 'n_33_quarter',
                          'w_0.3333333333333286', 'n_72_eighth', 'n_69_eighth', 'w_1/3',
                          'n_74_16th', 'n_70_16th', 'w_0.3333333333333286', 'n_74_eighth', 'n_70_eighth',
                          'w_0.3333333333333286', 'n_76_eighth', 'n_72_eighth', 'w_1/3', 'n_76_16th',
                          'n_72_16th', 'w_0.3333333333333286', 'n_76_16th', 'n_72_16th', 'n_33_quarter',
                          'w_0.3333333333333286', 'n_76_eighth', 'n_72_eighth', 'w_1/3', 'n_77_16th',
                          'n_74_16th', 'w_0.3333333333333286', 'n_77_eighth', 'n_74_eighth',
                          'w_0.3333333333333286', 'n_79_eighth', 'n_76_eighth', 'w_1/3', 'n_79_16th',
                          'n_76_16th', 'w_0.3333333333333286', 'n_76_eighth', 'n_35_quarter',
                          'w_0.5', 'n_77_eighth', 'n_74_16th', 'w_0.25', 'n_76_16th',
                          'w_0.25', 'n_77_eighth', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_79_16th',
                          'n_74_16th', 'w_0.25', 'n_76_16th',
                          'w_0.25', 'n_76_quarter', 'n_35_quarter', 'w_0.5', 'n_74_16th',
                          'w_0.25', 'n_76_16th',
                          'w_0.25', 'n_77_16th', 'n_76_eighth', 'w_0.25', 'n_76_eighth',
                          'w_0.25', 'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_76_eighth',
                          'n_35_quarter', 'w_0.5', 'n_77_eighth', 'n_74_16th', 'w_0.25',
                          'n_76_16th', 'w_0.25', 'n_77_eighth',
                          'w_0.25', 'n_76_16th', 'w_0.25', 'n_79_16th', 'n_74_16th', 'w_0.25', 'n_76_16th',
                          'w_0.25', 'n_81_eighth', 'n_35_quarter', 'w_0.5', 'n_79_16th', 'n_74_16th',
                          'n_81_16th', 'w_0.25', 'n_79_16th', 'n_76_16th', 'w_0.25', 'n_77_eighth',
                          'n_77_eighth', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_76_16th', 'n_74_16th',
                          'w_0.25', 'n_76_16th', 'w_0.25', 'n_74_quarter', 'n_33_quarter',
                          'w_0.5', 'n_72_16th',
                          'w_0.25', 'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_74_16th',
                          'w_0.25', 'n_72_16th', 'n_72_quarter', 'w_0.25', 'n_74_16th', 'w_0.25',
                          'n_33_quarter', 'w_0.5', 'n_72_eighth', 'w_0.25', 'n_74_16th',
                          'w_0.25', 'n_76_16th',
                          'n_72_eighth', 'w_0.25', 'n_74_16th', 'w_0.25', 'n_72_16th',
                          'w_0.25', 'n_74_16th', 'w_0.25', 'n_72_16th', 'n_69_16th',
                          'n_33_quarter', 'w_0.3333333333333286',
                          'n_72_eighth', 'n_69_eighth', 'w_1/3', 'n_74_16th', 'n_70_16th',
                          'w_0.3333333333333286', 'n_74_eighth', 'n_70_eighth',
                          'w_0.3333333333333286', 'n_76_eighth', 'n_72_eighth',
                          'w_1/3', 'n_76_16th', 'n_72_16th', 'w_0.3333333333333286', 'n_76_16th',
                          'n_72_16th', 'n_33_quarter', 'w_0.3333333333333286', 'n_76_eighth',
                          'n_72_eighth', 'w_1/3',
                          'n_77_16th', 'n_74_16th', 'w_0.3333333333333286', 'n_77_eighth', 'n_74_eighth',
                          'w_0.3333333333333286', 'n_79_eighth', 'n_76_eighth', 'w_1/3', 'n_79_16th',
                          'n_76_16th', 'w_0.3333333333333286', 'n_80_eighth', 'n_77_eighth', 'n_32_eighth',
                          'w_0.5', 'n_77_eighth', 'n_74_eighth', 'n_35_eighth', 'w_0.5', 'n_77_eighth',
                          'n_74_eighth', 'n_38_eighth', 'w_0.5', 'n_74_eighth', 'n_71_eighth',
                          'n_41_eighth',
                          'w_0.5', 'n_74_eighth', 'n_71_eighth', 'w_0.5', 'n_71_eighth', 'n_68_eighth',
                          'n_41_eighth', 'w_0.5', 'n_38_eighth', 'n_71_eighth', 'n_68_eighth', 'w_0.5',
                          'n_80_eighth', 'n_77_eighth', 'n_35_eighth', 'w_0.5',
                          'n_80_eighth', 'n_77_eighth',
                          'n_32_eighth', 'w_0.5', 'n_77_eighth', 'n_74_eighth', 'n_35_eighth',
                          'w_0.5', 'n_77_eighth', 'n_74_eighth', 'n_38_eighth', 'w_0.5',
                          'n_74_eighth', 'n_71_eighth', 'n_41_eighth', 'w_0.5', 'n_74_eighth',
                          'n_71_eighth', 'w_0.5', 'n_71_eighth', 'n_68_eighth',
                          'n_41_eighth', 'w_1.0', 'n_38_eighth', 'n_71_eighth', 'n_68_eighth',
                          'w_0.5', 'n_35_eighth', 'w_0.5', 'n_76_quarter', 'n_73_quarter',
                          'n_33_eighth', 'w_0.5', 'n_45_eighth', 'w_0.5',
                          'n_33_eighth', 'w_0.5', 'n_76_eighth', 'n_73_eighth', 'n_45_eighth', 'w_0.25',
                          'n_77_16th', 'n_74_16th', 'w_0.25', 'n_79_quarter', 'n_76_quarter', 'n_33_eighth',
                          'w_0.5', 'n_45_eighth', 'w_1.0', 'n_79_16th', 'n_76_16th', 'w_0.25', 'n_81_16th',
                          'n_77_16th', 'w_0.25', 'n_82_quarter', 'n_79_quarter', 'n_45_16th', 'w_0.25',
                          'n_43_16th', 'w_0.25', 'n_40_16th', 'w_0.25', 'n_33_16th', 'w_0.25', 'n_45_16th',
                          'w_0.25', 'n_43_16th', 'w_0.25', 'n_82_16th', 'n_79_16th', 'n_40_16th',
                          'w_0.25', 'n_84_16th', 'n_81_16th', 'n_33_16th', 'w_0.25',
                          'n_81_quarter', 'n_76_quarter',
                          'n_33_eighth', 'w_0.5', 'n_33_eighth', 'w_0.5', 'n_36_eighth', 'n_81_quarter',
                          'n_76_quarter', 'w_0.5', 'n_36_eighth', 'w_0.5', 'n_65_quarter', 'n_38_half',
                          'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_quarter', 'w_0.5', 'n_67_eighth', 'w_0.5',
                          'n_65_eighth', 'n_69_quarter', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_eighth',
                          'n_62_quarter', 'w_0.5', 'n_62_eighth', 'n_36_eighth',
                          'w_0.5', 'n_70_half', 'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5',
                          'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5',
                          'n_65_quarter', 'n_70_quarter', 'w_1.0', 'n_62_quarter', 'n_65_quarter', 'w_0.5',
                          'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half', 'w_0.5', 'n_60_eighth', 'w_0.5',
                          'n_64_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5', 'n_60_quarter',
                          'n_67_quarter', 'w_1.0', 'n_72_quarter', 'n_60_quarter', 'w_0.5', 'n_40_eighth',
                          'w_0.5', 'n_69_half', 'n_41_half', 'w_0.5', 'n_60_eighth', 'w_0.5', 'n_65_eighth',
                          'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_quarter', 'w_1.0', 'n_60_quarter',
                          'n_69_quarter', 'w_0.5', 'n_41_eighth', 'w_0.5', 'n_42_half', 'w_0.5',
                          'n_62_eighth',
                          'w_0.5', 'n_66_eighth', 'w_0.5', 'n_62_eighth', 'n_69_eighth', 'w_0.5',
                          'n_69_eighth', 'n_72_eighth', 'w_0.5', 'n_70_eighth', 'n_70_eighth', 'w_0.5',
                          'n_72_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_66_eighth',
                          'n_42_eighth', 'w_0.5', 'n_70_quarter', 'n_43_half', 'w_0.5', 'n_67_eighth',
                          'w_0.5', 'n_62_eighth', 'w_0.5', 'n_62_quarter', 'n_70_eighth', 'w_0.5',
                          'n_72_eighth', 'w_0.5', 'n_70_16th',
                          'n_72_16th', 'w_0.25', 'n_70_16th', 'w_0.25', 'n_67_quarter', 'n_69_eighth',
                          'w_0.5', 'n_62_eighth', 'n_43_eighth', 'w_0.5', 'n_65_quarter',
                          'n_44_half', 'w_0.5',
                          'n_65_quarter', 'w_0.5', 'n_59_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5',
                          'n_65_eighth', 'w_0.5', 'n_67_eighth', 'n_59_eighth', 'w_0.25',
                          'n_68_16th', 'w_0.25', 'n_67_eighth', 'n_68_eighth', 'w_0.5',
                          'n_65_eighth', 'n_65_eighth', 'n_44_eighth',
                          'w_0.5', 'n_65_quarter', 'n_62_quarter', 'n_45_quarter', 'w_1.0', 'n_33_quarter',
                          'w_0.5', 'n_65_16th', 'n_62_16th', 'w_0.25', 'n_67_16th', 'n_64_16th', 'w_0.25',
                          'n_64_quarter', 'n_61_quarter', 'w_2.0', 'n_41_16th', 'n_64_quarter',
                          'n_61_quarter', 'w_0.25', 'n_40_16th', 'w_0.25', 'n_38_16th',
                          'w_0.25', 'n_37_16th', 'w_0.25', 'n_65_quarter', 'n_38_half',
                          'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_quarter',
                          'w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_eighth', 'n_69_quarter',
                          'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_eighth', 'n_62_quarter',
                          'w_0.5', 'n_62_eighth', 'n_36_eighth', 'w_0.5',
                          'n_70_half', 'n_38_half', 'w_0.5', 'n_62_eighth',
                          'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_quarter',
                          'n_70_quarter', 'w_1.0', 'n_62_quarter', 'n_65_quarter', 'w_0.5',
                          'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half',
                          'w_0.5', 'n_60_eighth', 'w_0.5', 'n_64_eighth', 'w_0.5', 'n_65_eighth',
                          'w_0.5', 'n_60_quarter', 'n_67_quarter', 'w_1.0', 'n_72_quarter',
                          'n_60_quarter', 'w_0.5', 'n_40_eighth', 'w_0.5',
                          'n_69_half', 'n_41_half', 'w_0.5', 'n_60_eighth', 'w_0.5', 'n_65_eighth',
                          'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_quarter', 'w_1.0', 'n_60_quarter',
                          'n_69_quarter', 'w_0.5', 'n_41_eighth', 'w_0.5',
                          'n_42_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_66_eighth', 'w_0.5',
                          'n_62_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_72_eighth',
                          'w_0.5', 'n_70_eighth', 'n_70_eighth', 'w_0.5', 'n_72_eighth',
                          'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_66_eighth', 'n_42_eighth',
                          'w_0.5', 'n_70_quarter', 'n_43_half', 'w_0.5', 'n_67_eighth', 'w_0.5',
                          'n_62_eighth', 'w_0.5', 'n_62_quarter', 'n_70_eighth',
                          'w_0.5', 'n_72_eighth', 'w_0.5', 'n_70_16th', 'n_72_16th', 'w_0.25',
                          'n_70_16th', 'w_0.25', 'n_67_quarter', 'n_69_eighth',
                          ]

        random.shuffle(thousand_notes)

        for i in range(2, 7):
            for j in range(0, len(thousand_notes) - i):
                self.test_trie.add_list_to_trie(thousand_notes[j:j+i])

        for _ in range(0, 10000):
            lenght_of_prefix = random.randint(0, 4)
            prefix = []
            for j in range(0, lenght_of_prefix):
                prefix.append(thousand_notes[j])
            note = list(self.test_trie.return_choices(prefix).keys())
            new_music, _ = generate_music(self.test_trie, [], prefix)

            self.assertIn(new_music[0], note)

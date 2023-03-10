import unittest
import os.path
from midi.midi import midi_to_string, string_to_midi


class TestMidi(unittest.TestCase):
    def test_midi_to_str_to_midi(self):
        """
        muutetaan midi-tiedosto stringiksi, sitten takaisin midi-tiedostoksi ja vielä kerran stringiksi
        tarkistetaan, että ensimmäisellä ja toisella kerralla stringiksi käännetyt midi-tiedostot ovat samat
        koska ulkoinen kirjasto aiheuttaa pieniä muutoksia nuottien aika-arvoihin, niin testataan vain nuottien alkuosa
        """
        midi_file_to_string = midi_to_string(
            os.path.abspath("./src/tests/test.midi"))

        first_midi_as_list = midi_file_to_string.split()

        back_to_midi = string_to_midi(midi_file_to_string)
        back_to_midi.write("midi", "./src/tests/test2.midi")

        second_time_file_to_string = midi_to_string(
            os.path.abspath("./src/tests/test2.midi")
        )

        second_midi_as_list = second_time_file_to_string.split()

        for i in range(1, 100):
            self.assertEqual(
                first_midi_as_list[i].split("_", 2)[:1],
                second_midi_as_list[i].split("_", 2)[:1]
            )

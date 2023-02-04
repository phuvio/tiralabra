import unittest
import filecmp
import os.path
from midi.midi import midi_to_string, string_to_midi


class TestMidi(unittest.TestCase):
    def test_midi_to_str_to_midi(self):
        midi_file_to_string = midi_to_string(
            os.path.abspath("./src/tests/test.midi"))
        
        count_of_notes = len(midi_file_to_string.split())

        back_to_midi = string_to_midi(midi_file_to_string)
        back_to_midi.write("midi", "./src/tests/test2.midi")

        second_time_file_to_string = midi_to_string(
            os.path.abspath("./src/tests/test2.midi")
        )

        count_of_notes_second = len(second_time_file_to_string.split())

        self.assertEqual(count_of_notes, count_of_notes_second)
        self.assertEqual(midi_file_to_string, second_time_file_to_string)

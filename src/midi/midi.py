from fractions import Fraction
from music21.note import Note
import music21


def midi_to_string(midi_path):
    """Muuttaa midi-tiedoston str:ksi music21-kirjaston avulla

    Args:
        midi_path: midi-tiedoston sijainti

    Returns:
        str:ksi muutettu midi-tiedosto
    """

    score = music21.converter.parse(
        midi_path,
        quantizePost=True,
        quarterLengthDivisors=(4, 3))

    sequence_of_notes = ''

    last_offset = 0
    for note in score.flat.notes:
        delta = note.offset - last_offset
        duration = note.duration.components[0].type
        last_offset = note.offset
        if delta:
            sequence_of_notes += f'w_{delta} '
        notes = [note] if isinstance(note, Note) else note.notes
        for i in notes:
            sequence_of_notes += f'n_{i.pitch.midi}_{duration} '

    return sequence_of_notes


def string_to_midi(sequence_of_notes):
    """Muuttaa str:n midi-tiedostoksi music21-kirjaston avulla

    Args:
        sequence_of_notes: muutettava str

    Returns:
        midi-stream, joka voidaan tallentaa midi-tiedostoksi
    """

    stream = music21.stream.Stream()
    time = 1
    for i in sequence_of_notes.split():
        if i.startswith('n'):
            note, duration = i.lstrip('n_').split('_')
            new_note = music21.note.Note(int(note))
            new_note.duration.type = duration
            stream.insert(time, new_note)
        elif i.startswith('w'):
            time += float(Fraction(i.lstrip('w_')))

    return stream

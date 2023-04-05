import magenta.music as mm

def map_emotion_to_value(emotion):
    return (emotion - 1)/4
raw_values = [5, 5, 5, 5, 5]

emotion_values = [map_emotion_to_value(x) for x in raw_values]

notes = []

for value in emotion_values:
    pitch = int(60 + value * 24)

    velocity = 100
    duration = 1.0

    note = mm.NoteSequence.Note(
        pitch = pitch,velocity = velocity, start_time = len(notes), end_time = len(notes) + duration)
    notes.append(note)

sequence = mm.NoteSequence(notes = notes)

mm.midi_io.note_sequence_to_midi_file(sequence, 'emotion_note.mid')
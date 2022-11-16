from mido import MidiFile, MidiTrack


def read_midi_file(path):
    return MidiFile(path, clip=True)


def save_track_as_midi(track, path):
    mid = MidiFile()
    mid.tracks.append(track)
    mid.save(path)

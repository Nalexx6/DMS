from mido import MidiFile, MidiTrack
import numpy as np
import pandas as pd

def read_midi_file(path):
    return MidiFile(path, clip=True)


def np_to_csv(arr, path):
    pd.DataFrame(arr).to_csv(path, index=False, header=False)


def csv_to_np_array(path):
    return np.genfromtxt(path, delimiter=',').astype(int)


def save_track_as_midi(track, path):
    track.save(path)

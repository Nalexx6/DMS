import util
import converter as cvt

song_name = 'nocturne_27_2_(c)inoue'


if __name__ == "__main__":
    midi_path = f'{song_name}.mid'
    midi_new_path = f'{song_name}_new.mid'
    notes_path = f'notes_{song_name}.csv'
    tempos_path = f'tempos_{song_name}.csv'

    print("Reading Midi file")
    mid = util.read_midi_file(midi_path)

    print("Parsing notes and velocities")
    notes = cvt.extract_notes(mid)

    print("Parsing tempo changes")
    tempos = cvt.extract_tempos(mid)

    print("Saving notes")
    util.np_to_csv(notes, notes_path)
    print("Saving tempos")
    util.np_to_csv(tempos, tempos_path)

    print("=" * 100)

    print("Reading notes")
    notes = util.csv_to_np_array(notes_path)
    print("Reading tempos")
    tempos = util.csv_to_np_array(tempos_path)

    print(tempos)

    print("Generating track")
    new_mid = cvt.gen_mid(notes, tempos)

    print("Saving Midi file")
    util.save_track_as_midi(new_mid, midi_new_path)

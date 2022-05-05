import mido
from os import listdir
from os.path import join

mypath = "./midijam/"
midifiles = [f for f in listdir(mypath) if join(mypath, f)[-3:] == "mid"]

for midifile in midifiles:
    midi = mido.MidiFile(mypath + midifile)
    print(f"{midifile[:10] + '...' if len(midifile) > 10 else midifile}:\t\tType {midi.type}")
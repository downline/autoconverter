from pydub import AudioSegment
from math import ceil
import glob

fileext = ".mp3"

def formate(x, y):
    temp1 = "converted_songs/" + i.replace("songs\\", "").replace(fileext, "").replace(".", "").replace(",", "").replace("_", "") + " _" + str(ceil((len(song) / 1000.0))).zfill(3)
    return temp1
    
def editsong(x):
    temp2 = AudioSegment.from_file(i).fade_in(7000).fade_out(7000).set_frame_rate(44100)
    return temp2

for i in glob.glob("songs/*"):
    try:
        song = editsong(i)
        filepath = formate(i, song)
        song.export(filepath + ".ogg", format="ogg")
        print("Saved: " + filepath)
    except Exception as e:
        print("Wow, something broke: ", e)
        continue

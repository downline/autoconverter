from pydub import AudioSegment
from math import ceil
import glob

# Change targeted extension of a file to convert if needed.
fileext = ".mp3"

for i in glob.glob("songs/*" + fileext):
    try:
        song = AudioSegment.from_file(i).fade_in(7000).fade_out(7000).set_frame_rate(44100)
        filename = i.replace("songs\\", "").replace(fileext, "").replace(".", "").replace(",", "").replace("_", "") + " _" + str(ceil((len(song) / 1000.0))).zfill(3)
        filepath = "converted_songs/" + filename
        print("Converting:", filename)
        song.export(filepath + ".ogg", format="ogg")
    except Exception as e:
        print("Wow, something broke: ", e)
        input()


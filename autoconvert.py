from pydub import AudioSegment
from math import ceil
import glob

# Change targeted extension of a file to convert if needed.
fileext = ".mp3"

songlist = [f for f in glob.glob("songs/*" + fileext)]
i = 0
while i < len(songlist):
    try:
        file = songlist[i].replace('\\', '/')
        song = AudioSegment.from_file(file)
        editedsong = song.fade_in(7000).fade_out(7000).set_frame_rate(44100)
        editedsongduration = str(ceil((len(editedsong) / 1000.0))).zfill(3)
        oldfilename = file.replace("songs/", "").replace(fileext, "").replace(".", "").replace(",", "").replace("_", "")
        filename = oldfilename + " _" + editedsongduration
        filepath = "converted_songs/" + filename
        print("Converting:", oldfilename)
        editedsong.export(filepath + ".ogg", format="ogg")
        i +=1
        if i == len(songlist):
             input("Success. Out of the songs. Press enter to exit.")
        else:
            print("Success. Next.")
    except Exception as e:
        print("Wow, something broke: ", e)
        input()

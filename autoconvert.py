from pydub import AudioSegment
from math import ceil
import glob

songlist = [f for f in glob.glob("songs/*.mp3")]
i = 0
while i < len(songlist):
    try:
        file = songlist[i].replace('\\', '/')
        song = AudioSegment.from_file(file)
        editedsong = song.fade_in(7000).fade_out(7000).set_frame_rate(44100)
        editedsongduration = ceil((len(editedsong) / 1000.0))
        oldfilename = file.replace("songs/", "").replace(".mp3", "").replace(".", "").replace(",", "")
        filename = oldfilename + " _" + str(editedsongduration) + ".ogg"
        filepath = "converted_songs/" + filename
        print("Converting: ", filename)
        editedsong.export(filepath, format="ogg")
        i +=1
        if i == len(songlist):
             input("Success. Out of the songs. Press enter to exit.")
        else:
            print("Success. Next.")
    except Exception as e:
        print("Wow, something broke: ", e)
        input()

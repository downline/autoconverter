from pydub import AudioSegment
from math import ceil
import glob

songlist = [f for f in glob.glob("songs/*.mp3")]

i = 0
while i < len(songlist):
    try:
        songfile = songlist[i]
        songfileformatted = songfile.replace('\\', '/')
        song = AudioSegment.from_file(songfileformatted)
        songfaded = song.fade_in(7000).fade_out(7000)
        
        songfaded.duration_seconds == (len(song) / 1000.0) 
        songduration = ceil(songfaded.duration_seconds)
        print("Duration(SEC): ", songduration)
        
        songname0 = songfileformatted.replace("songs/", "")
        songname1 = songname0.replace(".mp3", "")
        songname2 = songname1.replace(".", "")
        songname3 = songname2 + " _" + str(songduration) + ".ogg"
        songpathname = "converted_songs/" + songname3
        
        print("Path and name: ", songpathname)
        songfaded.export(songpathname, format="ogg")
        print("Converted, doing the next one.")
        i += 1
    except Exception as e:
        print("Oopsie, something bad happened!", e)


from pydub import AudioSegment
from math import ceil
xd = 1
while xd == 1:
    try:
        fl = input("Name of your song: ")
        fxt = "songs/" + fl + ".mp3" 

        sng = AudioSegment.from_file(fxt)
        sfd = sng.fade_in(8000).fade_out(8000)
        
        sfd.duration_seconds == (len(sfd) / 1000.0) 
        cld = ceil(sfd.duration_seconds)
        
        flwtdt = fl.replace('.', '')
        
        flnm = "converted_songs/" + flwtdt + " _" + str(cld) + ".ogg"
        sfd.export(flnm, format='ogg')
        
        print(flnm, "has been created! \n")
        
    except Exception as e:
        print("You fucked up the path, didnt you?: ", e)
        

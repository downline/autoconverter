What this program does? It converts .mp3 to .ogg and adds fadein+fadeout automatically, along with getting time in a file name(needed so dynamo can play it). But it doesnt cut to "right parts", no. I havent yet learned neural networks to do such advanced things.


In case of:
1) using .py - install python(latest), add it to your path(checkbox), run install.bat, run in cmd "pip install pydub".
2) using .exe - run install.bat and that's all. (compiled with auto-py-to-exe)


install.bat is setting path for ffmpeg, so the whole script works. after using it, you shouldn't replace your folder. so just pick a good spot for it and dont move it elsewhere. it also can spam your $path, but dont worry, it shouldn't affect system at all(because it existed there this whole time, just hidden and some not). 
you dont need to clear it unless you're a perfectionist and you know what're you doing.


put your .mp3 files in "songs" folder, they will come out converted to ogg and edited in "converted_songs".


dont enter file extension in name selection part.


sorry for whole programm being fat, ffmpeg is too much for such easy task but i dont think there's anything better. feel free to suggest though


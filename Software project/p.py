import random
from pydub import AudioSegment
from pydub.playback import play

songs = ["/home/rajiv/project/1.m4a", "/home/rajiv/project/2.m4a", "/home/rajiv/project/3.m4a", "/home/rajiv/project/4.m4a", "/home/rajiv/project/5.m4a","/home/rajiv/project/6.m4a","/home/rajiv/project/7.m4a","/home/rajiv/project/8.m4a","/home/rajiv/project/9.m4a","/home/rajiv/project/10.m4a","/home/rajiv/project/11.m4a","/home/rajiv/project/12.m4a","/home/rajiv/project/13.m4a","/home/rajiv/project/14.m4a","/home/rajiv/project/15.m4a","/home/rajiv/project/16.m4a","/home/rajiv/project/17.m4a","/home/rajiv/project/18.m4a","/home/rajiv/project/19.m4a","/home/rajiv/project/20.m4a"]

while True:
    random.shuffle(songs)
    for song in songs:
        print("Name of the song :",song)
        s=AudioSegment.from_file(song)
        play(s)
        k=input("Enter c for continue or Enter q for quit :")
        if k=="c":
            continue
        elif k=="q":
            break
    if k=="q":
        break

        

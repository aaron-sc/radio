import sys
import glob, os

PATH = "/media/pi/"

sub_dirs = []
for dirs in os.walk(PATH):
    sub_dirs.append(dirs)
    
print(sub_dirs)

if("MUSIC" in sub_dirs):
    MEDIA_DIR = ""
    playlist = []

    os.chdir(PATH)

    for file in glob.glob("*.mp3"):
        playlist.append(PATH + str(file))

    print(playlist)
else:
    print("USB DEVICE NOT FOUND")
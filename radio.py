import sys
import glob, os

PATH = "/media/pi/"
sub_dirs = os.walk(PATH)

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
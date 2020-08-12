import sys
import glob, os
import subprocess

PATH = "/media/pi/"

sub_dirs = subprocess.getoutput("ls " + PATH)
print(sub_dirs.split("\n"))

if("MUSIC" in sub_dirs):
    MEDIA_DIR = "MUSIC"
    playlist = []

    os.chdir(PATH)

    for file in glob.glob("*.mp3"):
        playlist.append(PATH + str(file))

    print(playlist)
else:
    print("USB DEVICE NOT FOUND")
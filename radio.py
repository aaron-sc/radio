import sys
import glob, os

PATH = "/media/pi/MUSIC/"
playlist = []

os.chdir(PATH)

for file in glob.glob("*.mp3"):
    playlist.append(PATH + str(file))

print(playlist)
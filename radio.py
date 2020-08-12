import sys
import glob, os

PATH = "/media/pi/MUSIC"
music_files = []

os.chdir(path)

for file in glob.glob("*.mp3"):
    music_files.append(file)

print(music_files)
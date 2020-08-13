import sys
import glob, os
import subprocess
import random

# https://pimylifeup.com/raspberry-pi-pirate-radio/

FRQ = "108.0"
command = ""

# Below is playing the files
PATH = "/media/pi/"

sub_dirs = subprocess.getoutput("ls " + PATH).split("\n")

if("MUSIC" in sub_dirs):
    MEDIA_DIR = "MUSIC"
    playlist = []
    PATH = PATH + MEDIA_DIR + "/"
    os.chdir(PATH)

    for file in glob.glob("*.mp3"):
        playlist.append(PATH + str(file))

    random.shuffle(playlist)

    for song in playlist:
        command += "sox " + song + " -r 22050 -c 1 -b 16 -t wav - | sudo ~/fm_transmitter/fm_transmitter -f " + FRQ + " - && "
    command = command[:len(command)-3]

    print("PLAYING MUSIC")

    os.system(command)

else:
    print("USB DEVICE NOT FOUND")
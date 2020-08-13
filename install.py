import sys
import glob, os
import subprocess

# Below installs the FM player

print("Installing required packages")
os.system("sudo apt update && sudo apt install -y sox make gcc g++ git libmp3lame-dev")
os.chdir("~")
print("INSTALLING THE FM TRANSMITTER IN ~")
os.system("git clone https://github.com/markondej/fm_transmitter && cd fm_transmitter && make")

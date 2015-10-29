#!/usr/bin/python3

#
# Script name : wma_converter2_mp3.py
# Author : BDC
# Date : 26.10.15
# Description : script that will search through directories and find
#               wma files then convert to mp3
#

import os
import logging
import subprocess
import pipes
import sys

logging.basicConfig(filename='wma_converter2_mp3.log',level=logging.DEBUG)

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

#
# start of main code block
#

#
# list of all characters that will need to be escaped in with a filename or path to the file
#
reps = {" ":"\ ", "(":"\(", ")":"\)", "&":"\&", "£":"\£", "*":"\*", "!":"\!", "\'":"\\'"}
#
# Change the following to suit the root directory of where you want to search for 
# wma files from
#
basedir = "/bigfs/Music/"

for root, dirs, files in os.walk(basedir):
	for file in files:
		if file.endswith(".wma"):
			#
			# for every wma file we find under the basedir lets go through the following loop
			#
			dummy2 = os.path.join(root, file)
			#
			# Many of the music filenames have characters that are interpreted by the shell
			# so we need to search the path and filename for these characters and escape them
			#
			orig_path2file = replace_all(dummy2, reps)
			#
			# original filename will have a .wma extension, the newfilename will be the same
			# but with a .mp3 extension
			#
			new_path2file = orig_path2file.replace('.wma','.mp3')
			#
			# now lets build up the command line that we will be executing
			#
			command = "/usr/bin/mplayer -vo null -vc dummy -af resample=44100 -ao pcm:waveheader " + orig_path2file
			command = command + " && /usr/bin/lame -h -m s audiodump.wav -o " + new_path2file
			#
			# execute the built command using orig_path2file as i/p and new_path2file as o/p
			#
			p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate()[0]
			#
			# uncomment the following line if you just want to test on a single (first) file found
			#
			#sys.exit()

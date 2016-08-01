#!/usr/bin/python

import os
import sys
import smtplib
import subprocess
from sets import Set

# setting up a load of data sets with #1=cmd_line_stirng #2=Source_Dir #3=Dest_dir
backup_sets = ['do_photo','/Volumes/TheBigFive/Photos/','/mount/Photos/',\
		'do_video','/Volumes/TheBigFive/Video/','/mount/Video/',\
		'do_music','/Volumes/TheBigFive/Music/','/mount/Music/',\
		'do_audio','/Volumes/TheBigFive/AudioRecordings/','/mount/Audio/',\
		'do_mac','/Users/Bruce/','/mount/MacMini-BU']

sender = 'kiplingmini@brucecass.co.uk'
receivers = ['bruce.cass@piksel.com']

message = """From: KiplingMini <kiplingmini@brucecass.co.uk>
To: Bruce Cass <bruce.cass@piksel.com>
Subject: KiplingMini Backup Report

"""

# Try to get command line argument. This will identify which 
# mount point to be backed up
#
try:
	instr = sys.argv[1]
except:
	message = message + "\n*** Error: you forgot a command line arg!\n"
	sys.exit(2)

# Check to see if the script is already running. if it then bail
#
pid = str(os.getpid())
pidfile = "/tmp/sync2micro.pid"

if os.path.isfile(pidfile):
	message = message + "%s already exists, exiting" % pidfile
	sys.exit()

file(pidfile, 'w').write(pid)

try:
	# Script not already running therefore we will continue
	#
	if (instr in backup_sets):
		# command must be found in the array, therefore we can proceeed
		#
		# check to see if destination mount point exists
		#
		i = backup_sets.index(instr)
		#print "Index of found value is %d \n" %i
		source =  backup_sets[i+1]
		destin =  backup_sets[i+2]
		if os.path.ismount(destin):
			# mount point of destination exists! We should be good to go
			#
			message = message + "*************************************************\n"
			message = message + "**** Backing up %s to %s\n" % (source, destin)
			message = message + "*************************************************\n"
			cmdstring = "rsync -rva --stats %s %s" % (source, destin)
			proc = subprocess.Popen([cmdstring, ""], stdout=subprocess.PIPE, shell=True)
			(out, err) = proc.communicate()
			#result = os.system(cmdstring)
			message = message + out
		else:	
			message = message + "** Error: mount point %s does NOT exist! **\n" % destin
	else:
		message = message + "** Error: command %s does NOT exist in array **\n" % instr
	try:
   		smtpObj = smtplib.SMTP('192.168.1.106')
		smtpObj.sendmail(sender, receivers, message)         
		print "Successfully sent email"
	except SMTPException:
		print "Error: unable to send email"
finally:
	os.unlink(pidfile)

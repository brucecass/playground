#!/usr/bin/python

import os
import sys
import pycurl
import StringIO
import json
import pprint

# Try to get command line argument. This will identify which 
# mount point to be backed up
#
try:
        instr = sys.argv[1]
except:
        print "\n*** Error: you forgot a command line arg!\n"
        sys.exit(2)

# Ok so we must have at least one command line arg being passed in
# Build up URL
#
url = "https://pomstage.piksel.com/api/treehopper/resource/SERVER?c=privateIpAddress==" + instr

try:
	headers = { 'Authorization' : 'Basic dHJlZWhvcHBlci10ZXN0Ong4V1BxcTdza0JZczVlNUY' }
	response = StringIO.StringIO()
	remedy_call = pycurl.Curl()
	remedy_call.setopt(remedy_call.URL, url)
	remedy_call.setopt(remedy_call.WRITEFUNCTION, response.write)
	remedy_call.setopt(remedy_call.VERBOSE, 1)
	remedy_call.setopt(remedy_call.HTTPHEADER, ["%s: %s" % t for t in headers.items()])
	remedy_call.perform()

	http_code = remedy_call.getinfo(pycurl.HTTP_CODE)
	if http_code is 200:
		print response.getvalue()
		dictionary = json.loads(response.getvalue())
		print "\n\n\n\****************************Pretty o/p*************************************"
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(dictionary)
		print "*********************************************************************************"
	else:
		print "\n*** Error: Received something other than a HTTP 200 code back!\n"

	response.close()
	remedy_call.close()
except:
	print "\n*** Error: something went wrong with your call to Remedy!\n"

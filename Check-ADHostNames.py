"""
Check-ADHostNames.py
Takes a single argument of a filename, the file should contain a list of hostnames, one per line.
Returns only valid hostnames to standard out

for example, run:
Get-ADComputer -Filter * | select-object name | Out-File -Encoding UTF8 .\all-computers.txt

and pass the resultant file to this script to clean a list of AD computer names:
c:\tools\python\hostcheck.py .\all-computers.txt | Out-File .\valid-computers.txt
"""

import re
import sys
import codecs
import os

def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

if __name__ == "__main__":
	
	filename = sys.argv[1]
	
	with open(filename) as f:
		content = f.readlines()
	
		for line in content:
			line = line.strip()
			if is_valid_hostname(line):
				print (line)
			#print (str(line))

		f.close()
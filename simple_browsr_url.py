#This is the same simple_browser code with urllib
#Since HTTP is so common, we have a library that does all the socket 
#work for us and makes web pages look like a file.

import urllib
fhandle = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhandle:
	print line.strip()
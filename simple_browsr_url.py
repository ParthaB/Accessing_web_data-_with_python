#This is the same simple_browser code with urllib.

#Since HTTP is so common, we have a library that does all the
#socket work for us and makes web pages look like a file.

import urllib
fhandle = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhandle:
	print line.strip()

'''
OUTPUT:
Dean@Deans-Notebook:~/webdata_python$ python simple_browsr_url.py
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief

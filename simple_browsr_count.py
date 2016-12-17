import urllib
fhandle = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

count = dict()
for line in fhandle:
	words = line.split()
	for word in words:
		#dictionary get pattern
		count[word] = count.get(word, 0) + 1
print count 

'''
OUTPUT:
{'and': 3, 'envious': 1, 'already': 1, 'fair': 1, 'is': 3, 
'through': 1, 'pale': 1, 'yonder': 1, 'what': 1, 'sun': 2, 
'Who': 1, 'But': 1, 'moon': 1, 'window': 1, 'sick': 1, 
'east': 1, 'breaks': 1, 'grief': 1, 'with': 1, 'light': 1, '
It': 1, 'Arise': 1, 'kill': 1, 'the': 3, 'soft': 1, 'Juliet': 1}

import re
#handle = open('regex1.txt')

'''
for line in handle:
	line = line.rstrip() #rstrip() to clear the whitespaces 
	if re.search('^The.*', line):	
	#'^' is a special char to find all
	#beginning with 'The'
		print line 
Output:
There are at least three different algorithms that decide whether and how a given regex matches a string.
The oldest and fastest relies on a result in formal language theory that allows every nondeterministic finite automaton (NFA) to be transformed into a deterministic finite automaton (DFA). The DFA can be constructed explicitly and then run on the resulting input string one symbol at a time. 
Constructing the DFA for a regular expression of size m has the time and memory cost of O(2m), but it can be run on a string of size n in time O(n).
The third algorithm is to match the pattern against the input string by backtracking. This algorithm is commonly called NFA, but this terminology can be confusing. Its running time can be exponential, which simple implementations exhibit when matching against expressions like (a|aa)*b 
that contain both alternation and unbounded quantification and force the algorithm to consider an exponentially increasing number of sub-cases. This behavior can cause a security problem called Regular expression Denial of Service.
The three common quantifiers (*, + and ?) are greedy by default because they match as many characters as possible.[28] The regex ".*" applied to the string
The dot chatecter matches any charecter
The asterik means 'any number of times'
'''
'''
for line in handle:
	line = line.rstrip() #rstrip() to clear the whitespaces 
	if re.search('^The\S+', line):	
	#'^' is a special char to find all
	#beginning with 'The'
		print line

Output:
There are at least three different algorithms that decide whether and how a given regex matches a string.
'''
'''
x = 'My 2 favorite numbers are 7 and 66'
y = re.findall('[0-9]+', x)
print y

#Output:
#['2', '7', '66']

y = re.findall('[AEIOU]+', x)
print y

#Output:
#[]
'''

'''
x = 'From Stephen.marquisterdabili@uct.ac.za Sat Jan 5 09:14:16'
y = re.findall('\S+@\S+', x)

#greedy is a friend here. Find '@', push out on both sides, find 
#all the non-blank characters, stop at a blank, put the result in
#a list.

print y

#Output:
#['Stephen.marquisterdabili@uct.ac.za']
'''

'''
x = 'From Stephen.marquisterdabili@uct.ac.za Sat Jan 5 09:14:16'
y = re.findall('^From (\S+?@\S+)', x)

#Search starting with 'From', then a whitespace, 
#search for @', push out on both sides,
#find all the #non-blank characters, stop at a blank, 
#only return result in the parenthesis in a non-greedy manner.

print y

#Output:
#['Stephen.marquisterdabili@uct.ac.za']
'''

'''
handle = open('mbox-short.txt')

numlist = list()
for line in handle:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(stuff) != 1 : continue
	num = float(stuff[0])
	numlist.append(num)

print 'Maximum:', max(numlist)

#Output:
#Maximum = 0.9907
'''

'''
#test
for line in handle:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	print stuff
'''
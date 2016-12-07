import re

numlist = list()
total = 0
handle = open('regex_sum_42.txt')

for line in handle:
	line = line.rstrip()
	find_vals = re.findall('[0-9]+', line)
	numlist = numlist + find_vals
for i in numlist:
	total = total + int(i)
	'''
	if len(find_vals) > 0:

		results = int(find_vals[0])
		numlist.append(results)
		'''
print 'Sum:', total

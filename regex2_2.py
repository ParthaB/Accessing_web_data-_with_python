import re
numlist = list()
total = 0
handle = open('regex_sum_340738.txt')

for line in handle:
	line = line.rstrip()
	find_vals = re.findall('[0-9]+', line)
	numlist = numlist + find_vals
for i in numlist:
	total = total + int(i)

print 'Sum:', total

'''
print sum([int(i) for i in re.findall('[0-9]+', open('regex_sum_340738.txt').read())])
'''
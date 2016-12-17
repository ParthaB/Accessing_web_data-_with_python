#Examining response headers
#Week 3 assignment

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect takes only one argument.
mysock.connect(('www.data.pr4e.org', 80))
print 'Connected\n'

#get page with http/1.0 protocol, ENTER twice.
mysock.send('GET http://www.data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512) #retrieve upto 512 characters
	if(len(data) < 1):
		break
	print data

#shutdown before close is proper python protocol.
mysock.shutdown(socket.SHUT_RDWR)
mysock.close()
print 'Disconnected.\nBye, Bye'
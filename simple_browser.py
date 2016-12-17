#This is low level hardcode

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect takes only one argument.
mysock.connect(('www.py4inf.com', 80))
print 'Connected\n'

#get page with http/1.0 protocol, ENTER twice.
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512) #retrieve upto 512 characters
	if(len(data) < 1):
		break
	print data

#shutdown before close is proper python protocol.
mysock.shutdown(socket.SHUT_RDWR)
mysock.close()
print 'Disconnected.\nBye, Bye'

'''
OUTPUT:
Dean@Deans-Notebook:~/webdata_python$ python simple_browser.py
Connected

HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 167
Connection: close
Date: Sat, 17 Dec 2016 03:38:39 GMT
Server: Apache
Last-Modified: Fri, 04 Dec 2015 19:05:04 GMT
ETag: "a7-526172f5b5d89"
Accept-Ranges: bytes
Cache-Control: max-age=604800, public
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: origin, x-requested-with, content-type
Access-Control-Allow-Methods: GET

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and
 kill the envious moon
Who is already sick and pale with grief

Disconnected.
Bye, Bye
'''
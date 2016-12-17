import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect takes only one argument.
mysock.connect(('www.py4inf.com', 80))
print 'Connected'
mysock.shutdown(socket.SHUT_RDWR)
mysock.close()
print 'Disconnected. Bye, Bye'

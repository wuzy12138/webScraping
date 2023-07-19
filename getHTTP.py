import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#this command is in UTF-8
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # the newline is rule for http
#it sends Bytes
mysock.send(cmd)

while 1:
    #recv is receive
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
    
mysock.close()
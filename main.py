
import socket

sock = socket.socket()
sock.connect(('192.168.43.107', 9090))
sock.send(b'hello, world!')

data = sock.recv(1024)
sock.close()

print (data)
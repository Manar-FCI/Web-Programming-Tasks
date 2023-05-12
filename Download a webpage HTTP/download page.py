import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.facebook.com", 80))
s.send(b"GET/HTTP/1.1\r\nHost:www.facebook.com\r\n\r\n")
print(s.recv(4096).decode('utf-8'))

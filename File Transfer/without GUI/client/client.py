import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1234
client.connect((Host, Port))
file_name = client.recv(1024).decode('utf-8')
file_name = "file "+file_name
file = open(file_name, "wb")
data = client.recv(1024)
file.write(data)
file.close()



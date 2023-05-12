import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1234
s.bind((Host, Port))
s.listen(5)
client_socket, address = s.accept()
print(f"Connection to {address} established")
fileName = "manar.txt"
client_socket.send(fileName.encode('utf-8'))
file = open("manar.txt", "rb")
data = file.read()
client_socket.send(data)
file.close()
client_socket.close()


import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1234
client.connect((Host, Port))
file = open('galaxy.jpg', 'rb')
image_data = file.read(2048)
while image_data:
 client.send(image_data)
 image_data = file.read(2048)
file.close()
client.close()


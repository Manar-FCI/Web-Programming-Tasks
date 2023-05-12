import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1234
s.bind((Host, Port))
s.listen(5)
client_socket, address = s.accept()
print(f"Connection to {address} established")
name = input("Enter the name of the img: ")
ext = input("Enter the extension of your received file - jpg , png ,bmp: ")
nwImg = name + "." + ext
file = open(nwImg, "wb")
image_data = client_socket.recv(2048)
while image_data:
 file.write(image_data)
 image_data = client_socket.recv(2048)
file.close()
client_socket.close()








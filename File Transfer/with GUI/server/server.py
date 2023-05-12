import socket
HOST = ''  
PORT = 5000  
BUFFER_SIZE = 1024  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Server started and listening for connections...')

conn, addr = s.accept()
print('Connected by', addr)

with open('received_file.txt', 'wb') as f:
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        f.write(data)
print('File received successfully.')

conn.close()
s.close()
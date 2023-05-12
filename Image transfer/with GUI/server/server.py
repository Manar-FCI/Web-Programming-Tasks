import socket
import threading
from tkinter import *
from tkinter.messagebox import showinfo

HOST = ''  # Server IP address
PORT = 5000  # Server port number
BUFFER_SIZE = 4096  # Size of the buffer for receiving data
server_socket = None
client_socket = None
receive_thread = None

root = Tk()
root.geometry('300x150')
root.title('Server')

file_path = StringVar()
file_path.set('No image received')

file_label = Label(root, textvariable=file_path, wraplength=250)
file_label.pack(pady=10)

def receive_image():
    global server_socket, client_socket, receive_thread

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    client_socket, addr = server_socket.accept()
    receive_thread = threading.Thread(target=receive_image_thread)
    receive_thread.start()

def receive_image_thread():
    global client_socket, server_socket, file_path

    with open('received_image.jpg', 'wb') as f:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)

    client_socket.close()
    server_socket.close()

    file_path.set('received_image.jpg')
    showinfo('Success', 'Image received successfully.')

receive_button = Button(root, text='Receive Image', command=receive_image)
receive_button.pack(pady=10)

root.mainloop()
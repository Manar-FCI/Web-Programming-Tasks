import socket
import threading
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror

HOST = '127.0.0.1'  # Server IP address
PORT = 5000  # Server port number
BUFFER_SIZE = 4096  # Size of the buffer for sending data

client_socket = None
send_thread = None

root = Tk()
root.geometry('300x150')
root.title('Client')

file_path = StringVar()
file_path.set('No image selected')

file_label = Label(root, textvariable=file_path, wraplength=250)
file_label.pack(pady=10)

def select_image():
    global file_path
    path = filedialog.askopenfilename()
    file_path.set(path)

def send_image():
    global client_socket, send_thread

    if not file_path.get():
        showerror('Error', 'Please select an image to send.')
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        showerror('Error', 'Could not connect to server.')
        return

    send_thread = threading.Thread(target=send_image_thread)
    send_thread.start()

def send_image_thread():
    with open(file_path.get(), 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            client_socket.sendall(data)

    client_socket.close()

    showinfo('Success', 'Image sent successfully.')

select_button = Button(root, text='Select Image', command=select_image)
select_button.pack()

send_button = Button(root, text='Send Image', command=send_image)
send_button.pack(pady=10)

root.mainloop()
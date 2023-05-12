import socket
from tkinter import *
from tkinter import filedialog
HOST = '127.0.0.1'  
PORT = 5000  #
BUFFER_SIZE = 1024  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def select_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, END)
    file_entry.insert(0, file_path)

def send_file():
    file_path = file_entry.get()
    with open(file_path, 'rb') as f:
        s.connect((HOST, PORT))
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            s.sendall(data)
        s.close()

root = Tk()
root.geometry("360x160")

file_label = Label(root,  text='File:')
file_label.pack()

file_entry = Entry(root , width=40)
file_entry.pack()

file_button = Button(root, text='Select File' ,height=1, width=30, bg='white',fg='blue' , command=select_file)
file_button.pack()

send_button = Button(root, text='Send File',height=1, width=30, bg='white',fg='blue', command=send_file)
send_button.pack()

root.mainloop()
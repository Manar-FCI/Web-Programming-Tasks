import socket
import threading
import tkinter as tk

# Define constants
HOST = 'localhost'
PORT = 4444

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Ask the user for their name
name = input("What is your name? ")

# Send the user's name to the server
client_socket.send(bytes(name, "utf-8"))

# Function to receive messages from the server
def receive_messages():
    while True:
        message = client_socket.recv(1024).decode().strip()
        message_listbox.insert(tk.END, message)

# Function to send messages to the server
def send_message():
    message = message_entry.get()
    client_socket.send(bytes(message, "utf-8"))
    message_entry.delete(0, tk.END)

# Create the GUI
window = tk.Tk()
window.title("Chat Room")
window.geometry("400x400")

# Create the message listbox
message_listbox = tk.Listbox(window)
message_listbox.pack(fill=tk.BOTH, expand=True)

# Create the message entry box
message_entry = tk.Entry(window)
message_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Start receiving messages from the server in a separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start the GUI event loop
window.mainloop()
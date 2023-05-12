import socket
import threading

# Define constants
HOST = 'localhost'
PORT = 4444

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# List to keep track of connected clients and their names
client_list = []

# Function to handle each client connection
def client_thread(client_socket, client_address):
    # Ask the client for their name
    client_socket.send(bytes("What is your name?\n", "utf-8"))
    name = client_socket.recv(1024).decode().strip()

    # Add the client to the list of connected clients
    client_list.append((client_socket, name))

    # Send a welcome message to the new client
    client_socket.send(bytes("Welcome to the chat room, " + name + "!\n", "utf-8"))

    # Loop to receive and broadcast messages
    while True:
        # Receive a message from the client
        message = client_socket.recv(1024).decode().strip()

        # Check if the message is empty (i.e. the client has disconnected)
        if not message:
            break

        # Broadcast the message to all other connected clients
        for client in client_list:
            if client[0] != client_socket:
                client[0].send(bytes(name + ": " + message + "\n", "utf-8"))

    # Remove the client from the list of connected clients
    client_list.remove((client_socket, name))

    # Close the client socket
    client_socket.close()

# Function to listen for incoming connections and start a new thread for each client
def listen_for_clients():
    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()

        # Start a new thread to handle the client connection
        client_thread_thread = threading.Thread(target=client_thread, args=(client_socket, client_address))
        client_thread_thread.start()

# Start listening for incoming connections
listen_thread = threading.Thread(target=listen_for_clients)
listen_thread.start()
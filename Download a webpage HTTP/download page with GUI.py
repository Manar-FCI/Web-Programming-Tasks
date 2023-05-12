import socket
import tkinter as tk

def download():
    url = url_entry.get()

    # Parse the URL to get the host and path
    parts = url.split("/")
    host = parts[2]
    path = "/" + "/".join(parts[3:])

    # Create a socket and connect to the host
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 80))

    # Send an HTTP request to the server
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    sock.send(request.encode())

    # Receive the response from the server
    response = b""
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response += data

    # Close the socket
    sock.close()

    # Decode the response and display it in the GUI
    content = response.decode("utf-8")
    status_label.config(text="Downloaded successfully!")
    text_box = tk.Text(root)
    text_box.pack()
    text_box.insert(tk.END, content)
root = tk.Tk()
root.title("Web Page Downloader")

url_label = tk.Label(root, text="Enter the URL:" ,font=("Helvetica", 16))
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download",height=1, width=30, bg='white',fg='blue', command=download)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
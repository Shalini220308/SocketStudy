import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 8000))

# Display client socket details
print("Client connected from:", client_socket.getsockname())

# Receive message from server
server_message = client_socket.recv(1024).decode()
print("Received from server:", server_message)

# Send acknowledgement to server
client_socket.send("Acknowledgement received by client".encode())

# Close the connection
client_socket.close()
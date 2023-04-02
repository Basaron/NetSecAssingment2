import socket

# Define the server address and port
SERVER_ADDRESS = '192.168.0.167'
SERVER_PORT = 12345

# Define the size of the buffer for receiving data
BUFFER_SIZE = 1024

# Create a TCP socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the address and port
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# Listen for incoming client connections
server_socket.listen()

# Accept an incoming client connection
print('Waiting for a client connection...')
client_socket, client_address = server_socket.accept()
print('Connected to client at', client_address)

filename ='test.bin'

# Open a file for writing the received data
with open(filename, 'wb') as file:
    while True:
        # Receive data from the client
        data = client_socket.recv(BUFFER_SIZE)
        file.write(data)
        if not data:
            break

# Close the client socket and server socket
client_socket.close()
server_socket.close()

print('File transfer complete.')

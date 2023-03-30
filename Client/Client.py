import socket

# Define the server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 12345
CLIENT_ADDRESS = '127.0.0.2'
CLIENT_PORT = 12346

# Define the size of the buffer for sending data
BUFFER_SIZE = 1024

# Define the filename and file path for the file to be sent
filename = 'big_file.bin'
file_path = './' + filename

# Open the file and get its size
with open(file_path, 'rb') as file:
    file_data = file.read()
    file_size = len(file_data)

# Create a TCP socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.bind((CLIENT_ADDRESS, CLIENT_PORT))

# Connect to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Send the file data to the server in chunks
bytes_sent = 0
while bytes_sent < file_size:
    data = file_data[bytes_sent:bytes_sent+BUFFER_SIZE]
    client_socket.send(data)
    bytes_sent += len(data)

# Close the client socket
client_socket.close()

print('File transfer complete.')

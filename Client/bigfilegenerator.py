import os

# Define the size of the binary file to create in bytes
file_size = 1000* 1024 * 1024

# Generate random data for the binary file
data = os.urandom(file_size)

# Write the data to the binary file
with open('big_file.bin', 'wb') as file:
    file.write(data)
    
print('Big file created.')

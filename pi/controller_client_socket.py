import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Enter the host ip:')
port = 5005
s.connect((host, port))


while True:
    # Receive no more than 1024 bytes
    msg = s.recv(1024)
    unencoded_message = struct.unpack('i', msg)
    print(unencoded_message[0])

s.close()
import socket

from laptop.controller import Controller

TCP_IP = ''
TCP_PORT = 5005

#
# Initialize socket for communication
laptopOutput = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    laptopOutput.bind((TCP_IP, TCP_PORT))
except socket.error as e:
    print(str(e))
laptopOutput.listen(5)

conn, address = laptopOutput.accept()

controller = Controller()
controller.init(conn)
controller.listen()

import socket
import threading

#server is the ip addresss of the server
server = "192.168.56.1"
port = 3242
addr = (server, port)
# Make a socket using Inet protocol and stream type data connection
disconnectMsg = "!D"

header = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)


def send(msg):
    message = msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    print(send_length)
    client.send(message)
    print(client.recv(1024))  # We can also receive message from the server on the connection as its in Full duplex mode
    # i have provided fixed length but we can also have a dynamic approach to it like we had in server


send("Hello World!")
send(disconnectMsg)

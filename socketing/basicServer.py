import socket
import threading

# server is the ip address of the server
port, server = 3242, socket.gethostbyname(socket.gethostname())
addr = (server, port)
# Make a socket using Inet protocol and stream type data connection
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DisconnectMsg = "!D"
Server.bind(addr)  # Connect the socket to the server ip and port for further connections
header = 64


def handleClient(conn, addr):
    msg = ""
    print(f"New Connection with {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(header).decode(
            'utf-8')  # first we'll send a message containing the length of the actual data
        if msg_length:
            if msg == DisconnectMsg:
                connected = False
            else:
                msg_length = int(msg_length)
                # Then set our socket to listen for that amount of data so that we won't run out of length of message
                # received
                msg = conn.recv(msg_length).decode("utf-8")
                print(f"Address - {addr}, Message - {msg}")
                conn.send("Received Successfully".encode("utf-8"))  # We can also send message to the client via the
                # established connection
    conn.close()


def start():
    Server.listen()
    print(f"Server {server} is listening...")
    while True:
        conn, addr = Server.accept()
        print(f"Connected to {addr}")
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        # -1 as we already have an active thread of python running for our start def
        print(f"Active connections - ", threading.active_count() - 1)


print("Server starting...")
start()

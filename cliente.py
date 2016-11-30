import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('200.132.125.61', 54321))
data = input ( "SEND( TYPE q or Q to Quit):" )
if (data != 'Q' and data != 'q'):
    client_socket.send(data.encode())
else:
    client_socket.send(data)
    client_socket.close()
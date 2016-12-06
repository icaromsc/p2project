import socket
HOST = ''              # Endereco IP do Servidor
PORT = 54321            # Porta do Servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print('inicializando server...')
print 'endereco:',tcp.getsockname()[0],'\n porta:',PORT
while True:
    con, cliente = tcp.accept()
    print ('Concetado por', cliente)
    while True:
        msg = con.recv(1024).decode()
        if not msg: break
        print ('cliente:', msg)
    print ('Finalizando conexao do cliente', cliente)
    con.close()
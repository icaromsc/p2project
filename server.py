import socket
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 54321            # Porta do Servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print('inicializando server...')
print 'endereco:',tcp.getsockname()[0],'\nporta:',PORT
while True:
    con, cliente = tcp.accept()
    print ('Conectado por:', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print ('mensagem recebida:', msg)
    print ('Finalizando conexao do client:', cliente)
    con.close()


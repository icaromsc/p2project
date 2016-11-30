import socket
HOST = '200.132.125.64'     # Endereco IP do Servidor
PORT = 54321            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
#print ('Para sair use CTRL+X\n')
#msg = input()
'''while msg != '\x18': #CTRL+C
    tcp.send (msg)
    msg = input()'''
msg='digite uma mensagem'
tcp.send(msg)
tcp.close()
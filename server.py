import socket
import threading
import json
import controle
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 54321            # Porta do Servidor

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        print('openning server...')
        print 'endereco:', self.sock.getsockname()[0], '\nporta:', port

    def listen(self):
        print 'listening...'
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            print 'request delivered to thread'
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        print 'connected by:',address
        size = 1024
        try:
            data = client.recv(size)
            if data:
                # Set the response to echo back the recieved data
                response = data
                print 'response:',response
                print 'processing request'
                #c=controle.process_request(response,address)
                print 'teste'
                r = json.loads(response)
                tipo = r['tipo']
                print 'tipo de request:', tipo
                if tipo == 'pli':
                    # envia lista de arquivos
                    import client
                    files = controle.listarArquivos()
                    send = client.Sender(address, '')
                    send.sendListFiles(files)
                elif tipo == 'par':
                    # envia arquivo
                    gg = []
                #client.send(response)
                print 'finalize request'
            else:
                raise ('Client disconnected')
        except:
            client.close()
            return False



def process_request(response,adress):
    import client





def start():
    ThreadedServer(HOST, PORT).listen()


ThreadedServer(HOST, PORT).listen()
#start()

#if __name__ == "__main__":
#    port_num = input("Port? ")

'''tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    con.close()'''


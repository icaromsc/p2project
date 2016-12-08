import socket
import threading
#import json
import controle
import simplejson as json
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
                json_decode = response.replace("'", "\"")
                r = json.loads(json_decode)
                tipo = r['tipo']
                print 'tipo de request:', tipo
                if tipo == 'pli':
                    # envia lista de arquivos
                    import client
                    files = controle.listarArquivos()
                    send = client.Sender(address,'')
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
    #serve()
    ThreadedServer(HOST, PORT).listen()


ThreadedServer(HOST, PORT).listen()
#start()

#if __name__ == "__main__":
#    port_num = input("Port? ")

def serve():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    print('inicializando server...')
    print 'endereco:',tcp.getsockname()[0],'\nporta:',PORT
    print 'listening...'
    while True:
        con, address = tcp.accept()
        response = con.recv(1024)
        if not response: break
        print 'mensagem recebida:', response
        print 'Conectado por:', address
        json_decode= response.replace("'", "\"")
        r = json.loads(json_decode)
        print 'json:',r
        tipo = r['tipo']
        print 'tipo de request:', tipo
        if tipo == 'pli':
            # envia lista de arquivos
            import client
            files = controle.listarArquivos()
            send = client.Sender(address, 54321)
            con.close()
            send.sendListFiles(files)
        elif tipo == 'par':
            # envia arquivo
            gg = []
        # client.send(response)
            con.close()
        print 'finalize request...'
        print ('Finalizando conexao do client:', address)


#serve()
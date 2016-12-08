import socket
import threading
import json
import pcp
import time
import controle
#import yaml as json
HOST = ''              # Endereco IP do Servidor
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
            print 'waiting for request...'
            client, address = self.sock.accept()
            client.settimeout(60)
            print 'request delivered to thread'
            threading.Thread(target = self.processRequest,args = (client,address)).start()

    def processRequest(self, client, address):
        ip=address[0]
        print 'connected by:',ip
        size = 1024
        #try:
        data = client.recv(size)
        if data:
            # Set the response to echo back the recieved data
            response = data
            print 'response:',response
            print 'processing request'
            #c=controle.process_request(response,address)
            json_decode = response.replace("'", "\"")
            r = json.loads(json_decode)
            tipo = r['tipo']
            print 'tipo de request:', tipo
            import client
            if tipo == pcp.PEDIDO_LISTA_ARQUIVO :
                # envia lista de arquivos
                files = controle.listarArquivos()
                send = client.Sender(address,'')
                send.sendListFiles(files,ip)
            elif tipo == pcp.ENVIO_LISTA_ARQUIVO:
                # envia lista arquivo
                arquivos=r['dados']
                print 'recuperou do json lista:',arquivos
                #arquivos.append('gasparzinho.jpg')
                diff=controle.compararListas(arquivos)
                if not diff :
                    print 'diretorio sincronizado com cliente'
                else:
                    print 'preparando envio de requisicao dos arqs nao sincronizados'
                    for f in diff:
                        send = client.Sender(ip, str(f))
                        send.getFile()
                        time.sleep(1)
            #client.send(response)
            elif tipo == pcp.PEDIDO_ARQUIVO:
                arquivo = r['dados']
                print 'recuperou dados do json:', arquivo
                send = client.Sender(ip, arquivo)
                send.sendFile()
                print 'finalize request'

            elif tipo == pcp.ENVIO_ARQUIVO:
                dados = r['dados']
                print 'recuperou dados do json:', dados
                controle.saveFile(dados[0],controle.decode(dados[1]))


        else:
            raise ('Client disconnected')
        print 'finalizando thread...'
        #except:
            #client.close()
            #return False



def process_request(response,adress):
    import client





def start():
    #serve()
    ThreadedServer(HOST, PORT).listen()


ThreadedServer('', PORT).listen()
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
        if tipo == pcp.PEDIDO_LISTA_ARQUIVO:
            # envia lista de arquivos
            import client
            files = controle.listarArquivos()
            send = client.Sender(address, 54321)
            #con.close()
            send.sendListFiles(files,address)
        elif tipo == pcp.ENVIO_ARQUIVO:
            # envia arquivo
            gg = []
        elif tipo ==pcp.ENVIO_LISTA_ARQUIVO:
            d=[]
        # client.send(response)
            #con.close()
        print 'finalize request...'
        print ('Finalizando conexao do client:', address)


#serve()
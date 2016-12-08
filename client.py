import socket
import json
import jsons as j
import controle
#import aplicao as app
import threading as thread
import threading

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 54321            # Porta que o Servidor esta

class Sender(object):
    def __init__(self,host,filename):
        self.host=host
        self.filename=filename

    def sendFile(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (self.host, PORT)
        tcp.connect(dest)
        js = j.envioArq
        nome=self.filename
        file = controle.montaEnvioArq(nome)
        dados = [file.filename, file.data]
        js['dados'] = dados
        print str(js)
        msg = str(js)
        tcp.send(msg)
        tcp.close()

    def getFile(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (self.host, PORT)
        tcp.connect(dest)
        js = j.pedidoArq
        js['dados'] = self.filename
        print str(js)
        msg = str(js)
        tcp.send(msg)
        tcp.close()

    def sendListFiles(self,list):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (self.host, PORT)
        print  'preparando para enviar requsicao socket:', '\nip:', self.host, ' porta:', PORT
        try:
            js = j.envioListaArq
            js['dados'] = list
            print 'json a ser encaminhado:',str(js)
            msg = str(js)
            tcp.connect(dest)
            tcp.send(msg)
        except:
            print 'ERROR: deceiver no reached'
        tcp.close()

    def getListFiles(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print  'preparando para enviar requsicao socket:','\nip:',self.host,' porta:',PORT
        dest = (self.host, PORT)
        tcp.connect((self.host, PORT))
        js = j.pedidoListaArq
        print str(js)
        msg = str(js)
        print 'mensagem sendo enviada:',msg
        tcp.send(msg)
        tcp.close()

def start():
    import time
    while True:
        ips = controle.obter_ips()
        for ip in ips:
            threading.Thread(target=go,args=(ip)).start()
        time.sleep(5)


def go(ip):
    try:
        send = Sender(ip, 'golfinho.jpeg')
        send.getListFiles()
    except:
        print 'cliente ', ip, ' inalcansavel'


def testar():
    ips = controle.obter_ips()
    send = Sender(ips[1], 'golfinho.jpeg')
    send.getListFiles()
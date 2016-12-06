import socket
import json
import jsons as j
import aplicao as app
import threading as thread

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
        file = app.montaEnvioArq(nome)
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
        tcp.connect(dest)
        js = j.envioListaArq
        js['dados'] = list
        print str(js)
        msg = str(js)
        tcp.send(msg)
        tcp.close()

    def getListFiles(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (self.host, PORT)
        tcp.connect(dest)
        js = j.pedidoListaArq
        print str(js)
        msg = str(js)
        print 'mensagem sendo enviada:',msg
        tcp.send(msg)
        tcp.close()
send=Sender(HOST,'golfinho.jpeg')
send.getListFiles()
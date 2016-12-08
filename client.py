import socket
import json
import pcp
import controle
#import aplicao as app
import threading as thread
import threading
#from socket import *

mutex=threading.Lock()
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
        js = pcp.envioArq
        nome=self.filename
        file = controle.montaEnvioArq(nome)
        dados=[str(file.filename), file.data]
        js['dados'] = dados
        print str(js)
        msg = str(js)
        tcp.send(msg)
        tcp.close()

    def getFile(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (self.host, PORT)
        dados=[self.filename]
        tcp.connect(dest)
        js = pcp.pedidoArq
        js['dados'] = dados
        print str(js)
        msg = str(js)
        tcp.send(msg)
        tcp.close()

    def sendListFiles(self,list,host):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (host, PORT)
        print  'preparando para enviar requsicao socket:', '\nip:', self.host, ' porta:', PORT
        js = pcp.envioListaArq
        js['dados'] = list
        print 'json a ser encaminhado:',str(js)
        msg = str(js)
        tcp.connect(dest)
        tcp.send(msg)
        #print 'ERROR: deceiver no reached'
        print 'fechando conexao...'
        tcp.close()

    def getListFiles(self):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print  'preparando para enviar requsicao socket:','\nip:',self.host,' porta:',PORT
        dest = (self.host, PORT)
        tcp.connect((self.host, PORT))
        js = pcp.pedidoListaArq
        print str(js)
        msg = str(js)
        print 'mensagem sendo enviada:',msg
        tcp.send(msg)
        tcp.close()

def start():
    import time
    timeout=5
    while True:
        ips = controle.obter_ips()
        for ip in ips:
            time.sleep(timeout)
            threading.Thread(target=go,args=(ip,)).start()
            #value=(ip)
            #thread._start_new_thread(go,(ip))
        print 'aguardando timeout para novas solicitacoes...'
        time.sleep(timeout*len(ips))


def go(ip):
    #mutex = threading.Lock()
    #try:
    send = Sender(ip, '')
    #mutex.acquire()
    send.getListFiles()
    #mutex.release()
    #except:
        #mutex.acquire()
        #print 'cliente ', ip, ' inalcansavel'
        #mutex.release()

def testar():
    import time
    #ips = controle.obter_ips()

    send = Sender('localhost', '')
    send.getListFiles()
    '''while True:
        ips = controle.obter_ips()
        for ip in ips:
            time.sleep(2)
            send = Sender(ip, '')
            send.getListFiles()
        time.sleep(15)'''


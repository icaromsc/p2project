import os
import base64
import json
import tkFileDialog
ipFile='ips.txt'

import socket
#from Tkinter import Tk
#from tkFileDialog import askopenfilename


dirName = "public"
path = os.path.abspath(dirName)

#verfica se o diretorio inicial existe,caso contrario o cria e lista os arquivos
def listarArquivos():
    if not os.path.exists(path):
        print('nao existe diretorio!')
        print('criando diretorio...')
        os.mkdir(path)
    print ('listando diretorio compartilhado...')
    files=[]
    for nome in os.listdir(path):
        print (nome)
        files.append(nome)
    return files

#listarArquivos()


class PCP(object):
    def __init__(self):
        self.tipo=None
        self.id=None
        self.dados=None

    def __init__(self,t,i,d):
        self.tipo = t
        self.id = i
        self.dados = d



class FileShared(object):
    def __init__(self,filename,data):
        self.filename=filename
        self.data=data






def getFile():
    filename = tkFileDialog.askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print 'get file:',filename
    return filename

def getFileName(fileFullName):
    return os.path.basename(fileFullName)

def getDataFromFile(file):
    arq = open(file, 'rb')
    data = arq.read()
    arq.close()
    return data

def encode(file):
    return base64.b64encode(file)

def decode(base64File):
    return base64.b64decode(base64File)

def saveFile(filename, data):
    arq = open(path + '/' + filename, 'wb')
    arq.write(data)
    arq.close()


#TESTE COM JSON
'''dados=['arq1','arq2','arq3']
t=PCP('rli','',dados)

print'objeto normal:',t.__dict__
data=json.dumps(t.__dict__)
print'json:',data
with open('protocolo.json') as json_data:
    d = json.load(json_data)

    print d'''
# TESTE FILE CHOOSER
#tkinter().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = tkFileDialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)
def montaEnvioArq(filename):
    file=getDataFromFile(path+'/'+filename)
    dados=encode(file)
    arq=FileShared(filename,dados)
    return arq

def obterIps():
    print 'acessando lista de ips...'
    with open(ipFile, 'r') as f:
        data = f.read().splitlines()
        print data
        f.close()
        return data






''''#le array de bytres
arq=open(path+'/golfinho.jpeg','rb')
data=arq.read()
arq.close()
print data
#codifica para base64
encoded = base64.b64encode(data)
print encoded
#decodifica base64
decod= base64.b64decode(encoded)
arq=open(path+'_novo_golfinho.jpeg','wb')
arq.write(decod)
arq.close()
'''
obterIps()
#f=getFile()
#print 'filename:',getFileName(f)



    #links
#http://wiki.python.org.br/SocketBasico
#http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
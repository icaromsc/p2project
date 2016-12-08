import os
import base64
import json
import tkFileDialog
import pcp
import client
port='54321'
ipFile='ips.txt'
dirName = "public"
path = os.path.abspath(dirName)

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


def sharedFiles():
    files=[]
    for nome in os.listdir(path):
        files.append(nome)
    return files


def montaEnvioArq(filename):
    file=getDataFromFile(path+'/'+filename)
    dados=encode(file)
    arq=FileShared(filename,dados)
    return arq


def obter_ips():
    print 'acessando lista de ips...'
    with open(ipFile, 'r') as f:
        data = f.read().splitlines()
        print data
        f.close()
        return data

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


def compararListas(listaRecebida):
    listaLocal = sharedFiles()
    diff=set(listaRecebida).symmetric_difference(set(listaLocal))

    #c = set(listaRecebida).union(set(listaLocal))
    #d = set(listaRecebida).intersection(set(listaLocal))
    #diff = list(c - d)
    diff=list(diff)
    print 'difference between lists:' , diff
    return diff


def encode(file):
    return base64.b64encode(file)


def decode(base64File):
    return base64.b64decode(base64File)


def saveFile(filename, data):
    arq = open(path + '/' + filename, 'wb')
    arq.write(data)
    arq.close()
    print filename,' salvo em:',path






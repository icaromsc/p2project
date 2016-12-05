import os
import socket
import json
#from Tkinter import Tk
#import tkinter.ttk
#import tkinter.filedialog
import tkFileDialog
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
    for nome in os.listdir(path):
	    print (nome)
listarArquivos()

class PCP(object):
    def __init__(self):
        self.tipo=None
        self.id=None
        self.dados=None

    def __init__(self,t,i,d):
        self.tipo = t
        self.id = i
        self.dados = d



#TESTE COM JSON
dados=['arq1','arq2','arq3']
t=PCP('rli','',dados)

print('objeto normal:',t.__dict__)
data=json.dumps(t.__dict__)
print('json:',data)
with open('protocolo.json') as json_data:
    d = json.load(json_data)
    print(d)

# TESTE FILE CHOOSER
#tkinter().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = tkFileDialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

#links
#http://wiki.python.org.br/SocketBasico
#http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
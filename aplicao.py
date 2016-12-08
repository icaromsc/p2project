import os
import time
import controle
import base64
import json
import tkFileDialog
import socket
ipFile='ips.txt'
dirName = "public"
path = os.path.abspath(dirName)
print 'starting app...'
time.sleep(1)
import client
#client.start()
client.testar()









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

#f=getFile()
#print 'filename:',getFileName(f)





#links
#http://wiki.python.org.br/SocketBasico
#http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
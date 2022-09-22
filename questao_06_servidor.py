import socket, os, pickle
from pathlib import Path

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                         
porta = 9999

socket_servidor.bind((host, porta))
socket_servidor.listen()

def gerar_lista_arq(dir_arq):
    lista_arq = []
    for arq in os.scandir(dir_arq):
        # checa se o arquivo é uma pasta, para calcular seu tamanho
        check_dir = dir_arq +'/'+ arq.name
        if not Path(check_dir).is_dir():
            info = {}
            info['nome'] = arq.name
            info['size'] = arq.stat().st_size
            lista_arq.append(info)
    return lista_arq



print("Servidor de nome", host, "esperando conexao na porta", porta)
while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg = socket_cliente.recv(1024)
    diretorio = msg.decode('utf-8')

    lista_send = gerar_lista_arq(diretorio)

    bytes = pickle.dumps(lista_send)
    socket_cliente.send(bytes)
    print('Resposta enviada:', str(addr))
    socket_cliente.close()

socket_servidor.close()
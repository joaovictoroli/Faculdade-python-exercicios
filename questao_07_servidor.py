# cliente servidor udp
import socket
import psutil

HOST = ''
PORT = 9991 

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST, PORT)
udp.bind(orig)

print('Esperando receber na porta', PORT, '...')
while True:
    (msg, cliente) = udp.recvfrom(1024)
    print('Mensagem recebida, ', str(cliente))
    #print(cliente, msg.decode('ascii'))
    # Decodifica mensagem em UTF-8:
    if 'sair' == msg.decode('utf-8'):
        print("Fechando conexao com", str(cliente), "...")
        break
    elif 'info_memoria' == msg.decode('utf-8'):
        memoria = psutil.virtual_memory()
        msg_to_send = 'Memoria total: ' + str(round(memoria.total / 10**9, 2))  + 'GB \nMemoria disponivel: ' + str(round(memoria.available/  10**9, 2)) + 'GB'
    else:
        msg_to_send = "Falha na msg: " + msg.decode('utf-8')

    udp.sendto (msg_to_send.encode('utf-8'), cliente)
    print('Resposta enviada', str(cliente))

udp.close()
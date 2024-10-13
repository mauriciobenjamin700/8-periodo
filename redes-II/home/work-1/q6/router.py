import socket


from constants import RECEIVER, SENDER
from utils import decode_message

def Router(address: tuple, next_node: tuple, previous_node: tuple):
    """
    Cria um objeto socket e fica escutando mensagens vindas de um endereço específico e as direcionando para outro endereço.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(address)
    #sock.bind(ADDRESSES[ROUTER4])

    while True:
        data, _ = sock.recvfrom(4096)
        decode_data = decode_message(data)

        #print(f"Recebi {decode_data['message']} de {decode_data['owner']}")

        #print(f"Repassando mensagem para {ROUTER4} no endereço {ADDRESSES[ROUTER4]}")

    
        if decode_data["owner"] == SENDER:

            sock.sendto(data, next_node)

        elif decode_data["owner"] == RECEIVER:

            sock.sendto(data, previous_node)
    
            break # SE O SERVIDOR MANDOU, PODE ENCERRAR


    sock.close()

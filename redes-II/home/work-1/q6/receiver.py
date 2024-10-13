import socket
import json


from constants import ADDRESSES, RECEIVER, ROUTER4, SENDER, TURN_OFF_SERVER
from utils import decode_message, encode_message

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[RECEIVER])

    print("Aguardando mensagens...")

    num_messages = 0

    while True:
        data, _ = sock.recvfrom(4096)
        
        num_messages += 1

        decoded_message = decode_message(data)

        message = decoded_message['message']
        owner = decoded_message['owner']
        
        print(f"N {num_messages} Recebido: {message} de {owner}")

        if message == TURN_OFF_SERVER:

            print("Servidor Encerrando...")

            break

    to_sender = encode_message(num_messages, RECEIVER)

    sock.sendto(to_sender, ADDRESSES[ROUTER4])
    
    sock.close()

    print(f"Recebi {num_messages} mensagens")

if __name__ == "__main__":
    main()
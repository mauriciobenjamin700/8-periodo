import socket
import json


from constants import ADDRESSES, RECEIVER, ROUTER4, TURN_OFF_SERVER
from utils import decode_message, encode_message

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[RECEIVER])

    print("Aguardando mensagens...")

    num_messages = 0

    while True:
        data, _ = sock.recvfrom(4096)

        decoded_message = decode_message(data)

        message = decoded_message['message']
        #owner = deacoded_message['owner']
        
        #print(f"Recebido: {message} de {owner}")

        num_messages += 1

        if message == TURN_OFF_SERVER:

            print("Servidor Encerrando...")

            break

    to_sender = encode_message(str(num_messages), RECEIVER)

    sock.sendto(to_sender, ADDRESSES[ROUTER4])
    
    sock.close()

    print(f"Recebi {num_messages} mensagens")

if __name__ == "__main__":
    main()
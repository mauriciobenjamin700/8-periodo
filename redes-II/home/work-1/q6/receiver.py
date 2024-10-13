import socket
import json


from constants import ADDRESSES, RECEIVER
from utils import decode_message

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

        if message == "The End":

            print("Servidor Encerrando...")

            break
    
    sock.close()

    print(f"Recebi {num_messages} mensagens")

if __name__ == "__main__":
    main()
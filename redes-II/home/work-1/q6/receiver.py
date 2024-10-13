import socket
import json


from constants import ADDRESSES, RECEIVER
from utils import decode_message

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[RECEIVER])

    print("Aguardando mensagens...")

    while True:
        data, _ = sock.recvfrom(4096)

        decoded_message = decode_message(data)

        message = decoded_message['message']
        
        print(f"Recebido: {message}")

        if decoded_message["message"] == "The End":

            print("Recebido: The End")

            break
    
    sock.close()

if __name__ == "__main__":
    main()
import socket


from constants import ADDRESSES, RECEIVER, ROUTER1, ROUTER2, SENDER
from utils import decode_message

def main():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[ROUTER1])

    while True:
        data, _ = sock.recvfrom(4096)
        decode_data = decode_message(data)

        #print(f"Recebi {decode_data['message']} de {decode_data['owner']}")
        
        #print(f"Repassando mensagem para {ROUTER2} no endereço {ADDRESSES[ROUTER2]}")

        if decode_data["owner"] == SENDER:

            sock.sendto(data, ADDRESSES[ROUTER2])

        elif decode_data["owner"] == RECEIVER:

            sock.sendto(data, ADDRESSES[SENDER])

            break
    
    sock.close()

if __name__ == "__main__":
    main()
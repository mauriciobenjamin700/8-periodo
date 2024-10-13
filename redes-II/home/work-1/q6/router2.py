import socket


from constants import ADDRESSES, ROUTER2, ROUTER3
from utils import decode_message

def main():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[ROUTER2])

    while True:
        data, _ = sock.recvfrom(4096)
        decode_data = decode_message(data)

        print(f"Recebi {decode_data['message']} de {decode_data['owner']}")

        print(f"Repassando mensagem para {ROUTER3} no endereço {ADDRESSES[ROUTER3]}")
        sock.sendto(data, ADDRESSES[ROUTER3])
        
        if decode_data['message'] == "The End":
            break
    
    sock.close()

if __name__ == "__main__":
    main()
import socket


from constants import ADDRESSES, RECEIVER, ROUTER2, ROUTER3, ROUTER4, SENDER, TURN_OFF_ROUTERS
from utils import decode_message

def main():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[ROUTER3])

    while True:
        data, _ = sock.recvfrom(4096)
        decode_data = decode_message(data)

        #print(f"Recebi {decode_data['message']} de {decode_data['owner']}")

        
        #print(f"Repassando mensagem para {ROUTER4} no endereço {ADDRESSES[ROUTER4]}")

        if decode_data["owner"] == SENDER:

            sock.sendto(data, ADDRESSES[ROUTER4])

        elif decode_data["owner"] == RECEIVER:

            sock.sendto(data, ADDRESSES[ROUTER2])
        
            break
    
    sock.close()

if __name__ == "__main__":
    main()
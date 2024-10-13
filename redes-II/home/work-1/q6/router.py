import socket


from constants import ADDRESSES, RECEIVER, ROUTER3, ROUTER4, SENDER
from utils import decode_message

def Router(address: tuple, next_router: tuple, previous_router: tuple):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[ROUTER4])

    while True:
        data, _ = sock.recvfrom(4096)
        decode_data = decode_message(data)

        #print(f"Recebi {decode_data['message']} de {decode_data['owner']}")

        #print(f"Repassando mensagem para {ROUTER4} no endereço {ADDRESSES[ROUTER4]}")

    
        if decode_data["owner"] == SENDER:

            sock.sendto(data, ADDRESSES[RECEIVER])

        elif decode_data["owner"] == RECEIVER:

            sock.sendto(data, ADDRESSES[ROUTER3])
    
            break # SE O SERVIDOR MANDOU, PODE ENCERRAR


    sock.close()

if __name__ == "__main__":
    main()
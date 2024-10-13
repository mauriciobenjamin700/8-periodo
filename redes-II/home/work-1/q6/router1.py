import socket


from constants import ROUTER1
from utils import decode_message, get_next_step

def main():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(get_next_step(ROUTER1))

    while True:
        data, _ = sock.recvfrom(4096)
        decode_data = decode_message(data)

        print(f"Recebi {decode_data['message']} de {decode_data['owner']}")

        if decode_data['message'] == "The End":
            break

        sock.sendto(data, get_next_step(ROUTER1))
    
    sock.close()

if __name__ == "__main__":
    main()
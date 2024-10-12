import socket


from constants import SERVER_ADDRESS
from utils import decode_message, get_next_step

def main():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(SERVER_ADDRESS)

    while True:
        data, _ = sock.recvfrom(4096)
        decode_data = decode_message(data)
        if decode_data['message'] == "The End":
            break

        sock.sendto(data, get_next_step(decode_data['owner']))
    
    sock.close()

if __name__ == "__main__":
    main()
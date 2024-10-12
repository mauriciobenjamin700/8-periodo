import socket
from random import randint
from json import dumps


from checksum import calculate_checksum
from constants import NUM_MESSAGES,CLIENT_TO_SERVER_ADDRESS, MENSAGE_LENGTH

def generate_message() -> list[int]:
    return [randint(0, 1) for _ in range(MENSAGE_LENGTH)]

def main():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    for _ in range(NUM_MESSAGES):

        message = generate_message()

        checksum = calculate_checksum(message)

        data = dumps({'message': message, 'checksum': checksum})

        sock.sendto(data.encode(), CLIENT_TO_SERVER_ADDRESS)
    
    sock.close()

if __name__ == "__main__":
    main()
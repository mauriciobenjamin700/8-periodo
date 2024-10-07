import socket
import random
import json
from q4 import calculate_checksum

def generate_message(length=16):
    return [random.randint(0, 1) for _ in range(length)]

def main():
    n = 10  # Número de mensagens a serem enviadas
    server_address = ('receiver', 10000)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    for _ in range(n):
        message = generate_message()
        checksum = calculate_checksum(message)
        data = json.dumps({'message': message, 'checksum': checksum})
        sock.sendto(data.encode(), server_address)
    
    sock.close()

if __name__ == "__main__":
    main()
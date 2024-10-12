import socket
from json import loads


from checksum import calculate_checksum
from constants import NUM_MESSAGES, SERVER_ADDRESS

def main():
    NUM_MESSAGES

    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(SERVER_ADDRESS)
    
    errors = 0
    
    for _ in range(NUM_MESSAGES):

        data, _ = sock.recvfrom(4096)

        received = loads(data.decode())

        message = received['message']

        received_checksum = received['checksum']

        calculated_checksum = calculate_checksum(message)
        
        if received_checksum != calculated_checksum:
            errors += 1
    
    sock.close()
    
    if errors == 0:
        print(f"Nenhum erro detectado nas {NUM_MESSAGES} mensagens enviadas.")
    else:
        print(f"Erro detectado em {errors} mensagens de {NUM_MESSAGES}.")

if __name__ == "__main__":
    main()
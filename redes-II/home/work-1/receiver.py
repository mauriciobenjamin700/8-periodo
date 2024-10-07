import socket
import json
from q4 import calculate_checksum

def main():
    n = 10  # Número de mensagens a serem recebidas
    server_address = ('0.0.0.0', 10000)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    
    errors = 0
    
    for _ in range(n):
        data, _ = sock.recvfrom(4096)
        received = json.loads(data.decode())
        message = received['message']
        received_checksum = received['checksum']
        calculated_checksum = calculate_checksum(message)
        
        if received_checksum != calculated_checksum:
            errors += 1
    
    sock.close()
    
    if errors == 0:
        print("Nenhum erro detectado nas mensagens enviadas.")
    else:
        print(f"Erro detectado em {errors} mensagens.")

if __name__ == "__main__":
    main()
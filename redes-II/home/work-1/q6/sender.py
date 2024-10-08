import socket
import random
import json
import time
from datetime import datetime, timedelta


from constants import MENSAGE_LENGTH, TIME_TO_SEND

def generate_message() -> list[int]:
    return [random.randint(0, 1) for _ in range(MENSAGE_LENGTH)]

def main() -> None:
    server_address = ('node1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    end_time = datetime.now() + timedelta(minutes=TIME_TO_SEND)
    
    while datetime.now() < end_time:
        message = generate_message()
        data = json.dumps({'message': message})
        sock.sendto(data.encode(), server_address)
        time.sleep(1)  # Envia uma mensagem por segundo
    
    # Enviar mensagem de encerramento
    sock.sendto("The End".encode(), server_address)
    sock.close()

if __name__ == "__main__":
    main()
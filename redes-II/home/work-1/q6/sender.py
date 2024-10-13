import socket
import random
import time
from datetime import datetime, timedelta


from constants import (
    ADDRESSES,
    MENSAGE_LENGTH,
    ROUTER1,
    SENDER, 
    TIME_TO_SEND
)
from utils import encode_message


def generate_message() -> list[int]:
    return [random.randint(0, 1) for _ in range(MENSAGE_LENGTH)]

def main() -> None:

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    end_time = datetime.now() + timedelta(minutes=TIME_TO_SEND)

    num_messages = 0

    print(f"Enviando mensagens por {TIME_TO_SEND} minutos...")

    while datetime.now() < end_time:
        
        message = generate_message()
        data = encode_message(message, SENDER)

        #print(f"Enviando: {message} para {ROUTER1} no endereço {ADDRESSES[ROUTER1]}")

        sock.sendto(data, ADDRESSES[ROUTER1])
        num_messages += 1
        time.sleep(1)  # Envia uma mensagem por segundo
    
    # Enviar mensagem de encerramento

    message = "The End"

    data = encode_message(message, SENDER)

    #print(f"Enviando: {message} para {ROUTER1} no endereço {ADDRESSES[ROUTER1]}")

    sock.sendto(data, ADDRESSES[ROUTER1])
    sock.close()

    num_messages += 1

    print(f"Enviei {num_messages} mensagens")

if __name__ == "__main__":
    main()
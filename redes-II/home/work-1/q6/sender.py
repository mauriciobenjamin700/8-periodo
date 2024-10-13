import socket
import random
import json
import time
from datetime import datetime, timedelta


from constants import (
    MENSAGE_LENGTH,
    SENDER, 
    TIME_TO_SEND,
    ADDRESSES,
    ROUTER1
)
from utils import (
    get_next_step, 
    encode_message, 
    decode_message
)

def generate_message() -> list[int]:
    return [random.randint(0, 1) for _ in range(MENSAGE_LENGTH)]

def main() -> None:

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(get_next_step(SENDER))

    end_time = datetime.now() + timedelta(minutes=TIME_TO_SEND)

    print(f"Enviando mensagens por {TIME_TO_SEND} minutos...")

    while datetime.now() < end_time:
        
        message = generate_message()
        data = encode_message(message, SENDER)

        print(f"Enviando: {message}")

        sock.sendto(data, get_next_step(SENDER))
        time.sleep(1)  # Envia uma mensagem por segundo
    
    # Enviar mensagem de encerramento

    message = "The End"

    data = encode_message(message, SENDER)

    sock.sendto(data, get_next_step(SENDER))
    sock.close()

if __name__ == "__main__":
    main()
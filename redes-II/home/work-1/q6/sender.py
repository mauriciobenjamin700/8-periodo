import socket
import random
import time
from datetime import datetime, timedelta


from constants import (
    ADDRESSES,
    MENSAGE_LENGTH,
    RECEIVER,
    ROUTER1,
    SENDER, 
    TIME_TO_SEND,
    TURN_OFF_SERVER
)
from utils import decode_message, encode_message


def generate_message() -> list[int]:
    return [random.randint(0, 1) for _ in range(MENSAGE_LENGTH)]

def main() -> None:

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[SENDER])

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

    message = TURN_OFF_SERVER
    data = encode_message(message, SENDER)
    #print(f"Enviando: {message} para {ROUTER1} no endereço {ADDRESSES[ROUTER1]}")
    sock.sendto(data, ADDRESSES[ROUTER1])
    num_messages += 1
    
    # Recebendo o retorno do servidor
    data, _ = sock.recvfrom(4096)
    decode_data = decode_message(data)
    num_messages_server = decode_data["message"]
    server_name = decode_data["owner"]
    sock.close()


    print(f"Enviei {num_messages} mensagens")
    print(f"Servidor {server_name} recebeu {num_messages_server} mensagens")

if __name__ == "__main__":
    main()
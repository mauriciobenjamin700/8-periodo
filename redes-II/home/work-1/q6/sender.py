import os
import socket
import random
import time
from datetime import datetime, timedelta
import statistics

from constants import (
    ADDRESSES,
    MENSAGE_LENGTH,
    ROUTER1,
    SENDER, 
    TIME_TO_SEND,
    TURN_OFF_SERVER
)
from utils import decode_message, encode_message


def generate_message() -> list[int]:
    return [random.randint(0, 1) for _ in range(MENSAGE_LENGTH)]

def metrics(sended_messages: int, received_messages: int, timestamps: list[float]) -> str:
    # Calcular taxas de recebimento por segundo
    intervals = [timestamps[i] - timestamps[i - 1] for i in range(1, len(timestamps))]
    rates = [1 / interval for interval in intervals] if intervals else [0]

    max_rate = max(rates) if rates else 0
    min_rate = min(rates) if rates else 0
    avg_rate = sum(rates) / len(rates) if rates else 0
    std_dev_rate = statistics.stdev(rates) if len(rates) > 1 else 0

    metrics_output = (
        "-"*50 + "\n"
        f"Métricas obtidas em {TIME_TO_SEND}min:\n"
        f"Enviadas: {sended_messages}\n"
        f"Recebidas: {received_messages}\n"
        f"Perdidas: {sended_messages - received_messages}\n"
        f"Porcentagem de perda: {((sended_messages - received_messages) / sended_messages) * 100}%\n"
        f"Média de mensagens enviadas por minuto: {round(sended_messages / TIME_TO_SEND,0)}\n"
        f"Média de mensagens recebidas por segundo: {round(received_messages / (TIME_TO_SEND * 60),0)}\n"
        f"Taxa de recebimento máxima: {max_rate:.2f}\n"
        f"Taxa de recebimento mínima: {min_rate:.2f}\n"
        f"Taxa de recebimento média: {avg_rate:.2f}\n"
        f"Desvio padrão da taxa de recebimento: {std_dev_rate:.2f}\n"
        "-"*50 + "\n"
    )

    return metrics_output

  

def save_metrics(result: str, filename: str = "metrics.txt") -> None:
    if not os.path.exists("metrics"):
        os.makedirs("metrics")
    with open(os.path.join("metrics", filename), "w") as file:
        file.write(result)


def main() -> None:

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(ADDRESSES[SENDER])

    end_time = datetime.now() + timedelta(minutes=TIME_TO_SEND)

    num_messages = 0
    timestamps = []

    print(f"Enviando mensagens por {TIME_TO_SEND} minutos...")

    while datetime.now() < end_time:
        
        message = generate_message()
        data = encode_message(message, SENDER)

        #print(f"Enviando: {message} para {ROUTER1} no endereço {ADDRESSES[ROUTER1]}")

        sock.sendto(data, ADDRESSES[ROUTER1])
        num_messages += 1
        timestamps.append(time.time())
        
        #time.sleep(1)  # Envia uma mensagem por segundo (Garante e entrega das msgs)
        #time.sleep(0.1)  # (Garante e entrega de mais msgs)
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
    sock.close()

    result = metrics(num_messages, num_messages_server, timestamps)

    print(result)

    save_metrics(result)

if __name__ == "__main__":
    main()
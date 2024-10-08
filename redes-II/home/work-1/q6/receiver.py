import socket
import json


from constants import SERVER_ADDRESS

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(SERVER_ADDRESS)
    
    while True:
        data, _ = sock.recvfrom(4096)
        if data.decode() == "The End":
            print("Recebido: The End")
            break
        received = json.loads(data.decode())
        message = received['message']
        print(f"Recebido: {message}")
    
    sock.close()

if __name__ == "__main__":
    main()
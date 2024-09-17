# Protocolos

Sempre evitar usar postar com númeração a baixo de 1024, pois geralmente as portas de 0 até 1024 são usadas pelo sistema operacional

## User Datagram Protocol - UDP

- Não orientado a conexão
- Não confiável
- Exemplos de serviços que usam  UDP
  - stream de áudio
  - FTP
  - DNS
  - NFS

### Código - UDP

#### Cliente - UDP

```python
import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = "Hello, Server"
clientSocket = socket.socket(socket.AF_INET, socket.SOCKE_DGRAM)
clientSocket = sendto(Message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
```

#### Servidor - UDP

```python
import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = ServerSock.recvfrom(1024)
    print("Message: ", data, "End. Cliente: ", addr)
```

## Transmission Control Protocol - TCP

- Orientado à conexão
- Confiável
- Exemplos de serviços que usam TCP:
  - HTTP
  - Email
  - Canais de controle de media

### Código - TCP

#### Cliente - TCP

```python
import socket
HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for x in range(10):
        s.sendall(b"Hello, World")
        data = s.recv(1024)
        print("Recebido: ", data)
```

#### Servidor

```python
import socket
HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Conectado com ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

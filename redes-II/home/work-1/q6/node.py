import socket


from constants import SERVER_ADDRESS

def main():
    node_name = socket.gethostname()
    next_node = {
        'node1': ('node2', 10000),
        'node2': ('node3', 10000),
        'node3': ('node4', 10000),
        'node4': ('receiver', 10000)
    }
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(SERVER_ADDRESS)
    
    while True:
        data, _ = sock.recvfrom(4096)
        if data.decode() == "The End":
            break
        sock.sendto(data, next_node[node_name])
    
    sock.close()

if __name__ == "__main__":
    main()
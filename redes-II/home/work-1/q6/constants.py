MENSAGE_LENGTH = 16
TIME_TO_SEND = 1 # tempo em minutos para enviar as mensagens, onde o ideial seria 5 minutos
START_NODE_ADDRESS = ('node1', 10000)
SERVER_ADDRESS = ('receiver2', 10000)
USERS = [
    "sender2",
    "node1",
    "node2",
    "node3",
    "node4",
    "receiver2"
]

STEPS = {
    'sender2':('node1', 10000),  # Endereço do próximo nó e porta do próximo nó
    'node1':  ('node2', 10000),
    'node2':  ('node3', 10000),
    'node3':  ('node4', 10000),
    'node4':  ('receiver2', 10000) 
}
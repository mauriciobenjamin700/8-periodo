MENSAGE_LENGTH = 16
TIME_TO_SEND = 1  # tempo em minutos para enviar as mensagens, onde o ideal seria 5 minutos
START_NODE_ADDRESS = ('router-1', 10000)
SERVER_ADDRESS = ('0.0.0.0', 10005)
USERS = [
    "sender-q6",
    "router-1",
    "router-2",
    "router-3",
    "router-4",
    "receiver-q6"
]

# STEPS = {
#     'sender-q6': ('router-1', 10001),  # Endereço do próximo nó e porta do próximo nó
#     'router-1':  ('router-2', 10002),
#     'router-2':  ('router-3', 10003),
#     'router-3':  ('router-4', 10004),
#     'router-4':  ('receiver-q6', 10005)
# }

STEPS = {
    'sender-q6': ('0.0.0.0', 10001),  # Endereço do próximo nó e porta do próximo nó
    'router-1':  ('0.0.0.0', 10002),
    'router-2':  ('0.0.0.0', 10003),
    'router-3':  ('0.0.0.0', 10004),
    'router-4':  ('0.0.0.0', 10005)
}
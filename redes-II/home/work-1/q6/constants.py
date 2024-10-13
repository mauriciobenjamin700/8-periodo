MENSAGE_LENGTH = 16
TIME_TO_SEND = 1  # tempo em minutos para enviar as mensagens, onde o ideal seria 5 minutos


SENDER = 'sender-q6'
ROUTER1 = 'router-1'
ROUTER2 = 'router-2'
ROUTER3 = 'router-3'
ROUTER4 = 'router-4'
RECEIVER = 'receiver-q6'

ADDRESSES = {
    
    SENDER:    ('sender-q6', 10000),  
    ROUTER1:   ('router-1', 10001),
    ROUTER2:   ('router-2', 10002),
    ROUTER3:   ('router-3', 10003),
    ROUTER4:   ('router-4', 10004),
    RECEIVER:  ('receiver-q6', 10005)
}

STEPS = {
    SENDER: ADDRESSES[ROUTER1],  
    ROUTER1:  ADDRESSES[ROUTER2],
    ROUTER2:  ADDRESSES[ROUTER3],
    ROUTER3:  ADDRESSES[ROUTER4],
    ROUTER4:  ADDRESSES[RECEIVER]
}

TURN_OFF_SERVER = "The End"
TURN_OFF_ROUTERS = "turnoff"
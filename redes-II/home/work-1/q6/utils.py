from json import dumps, loads


from constants import STEPS

def encode_message(message: list[int], owner: str) -> bytes:
    datagram = {'message': message, 'owner': owner}
    return dumps(datagram).encode()

def decode_message(datagram: bytes) -> dict:
    return loads(datagram.decode())

def get_next_step(now: str):
        
    if now == 'sender2':
        return STEPS['sender2']
    elif now == 'node1':
        return STEPS['node1']
    elif now == 'node2':
        return STEPS['node2']
    elif now == 'node3':
        return STEPS['node3']
    elif now == 'node4':
        return STEPS['node4']
    else:
        return None

        
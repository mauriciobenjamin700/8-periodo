from json import dumps, loads


from constants import STEPS, USERS

def encode_message(message: list[int], owner: str) -> bytes:
    datagram = {'message': message, 'owner': owner}
    return dumps(datagram).encode()

def decode_message(datagram: bytes) -> dict:
    return loads(datagram.decode())

def get_next_step(now: str):
        
    if now == USERS[0]:
        return STEPS[USERS[0]]
    elif now == USERS[1]:
        return STEPS[USERS[1]]
    elif now == USERS[2]:
        return STEPS[USERS[2]]
    elif now == USERS[3]:
        return STEPS[USERS[3]]
    elif now == USERS[4]:
        return STEPS[USERS[4]]
    else:
        return None

        
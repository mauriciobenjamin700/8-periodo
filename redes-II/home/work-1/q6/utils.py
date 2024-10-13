from json import dumps, loads


from constants import STEPS

def encode_message(message: list[int], owner: str) -> bytes:
    datagram = {'message': message, 'owner': owner}
    return dumps(datagram).encode()

def decode_message(datagram: bytes) -> dict:
    return loads(datagram.decode())

def get_next_step(now: str):
    
    if now in STEPS.keys():

        return STEPS[now]
    
    else:

        raise ValueError(f"Nó {now} não está na lista de passos.")

        
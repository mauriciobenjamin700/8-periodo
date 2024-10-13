from json import dumps, loads


def encode_message(message: list, owner: str) -> bytes:
    datagram = {'message': message, 'owner': owner}
    return dumps(datagram).encode()

def decode_message(datagram: bytes) -> dict:
    return loads(datagram.decode())

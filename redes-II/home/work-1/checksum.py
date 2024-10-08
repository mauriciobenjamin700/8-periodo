from random import randint


from constants import MENSAGE_LENGTH
def generate_bits() -> list[int]:
    """
    Gera uma sequência aleatória de bits com tamanho 16.
    """
    return [randint(0, 1) for _ in range(MENSAGE_LENGTH)]

def calculate_checksum(bits: list[int]) -> int:    
    """
    O cálculo do checksum no  é feito de forma interativa, bit a bit, utilizando a operação XOR. 

    Inicialização do Checksum:

    O checksum é inicializado com o valor 0.

    O checksum é inicializado com zero porque o valor inicial de um checksum deve ser neutro para a operação que será aplicada. No caso da operação XOR, o valor neutro é zero. Isso ocorre porque:

    Iteração sobre os Bits:

    O código percorre cada bit na lista de bits gerados.
    Para cada bit, o checksum é atualizado usando a operação XOR (^).
    Operação XOR:

    A operação XOR (ou "exclusive or") é uma operação lógica que retorna 1 se os bits comparados forem diferentes e 0 se forem iguais.
    Quando aplicada bit a bit, a operação XOR tem a propriedade de cancelar bits iguais e manter bits diferentes.
    Exemplo de Cálculo
    Suponha que a lista de bits gerados seja [1, 0, 1, 1].

    Inicialmente, o checksum é 0.
    Iteração 1: checksum = 0 XOR 1 = 1
    Iteração 2: checksum = 1 XOR 0 = 1
    Iteração 3: checksum = 1 XOR 1 = 0
    Iteração 4: checksum = 0 XOR 1 = 1
    O checksum final é 1.

z   
    """
    checksum = 0
    for bit in bits:
        checksum ^= bit  # XOR bit a bit
    return checksum

def main():
    bits = generate_bits()
    print(f"Bits gerados: {bits}")
    
    checksum = calculate_checksum(bits)
    print(f"Checksum: {checksum}")

if __name__ == "__main__":
    main()
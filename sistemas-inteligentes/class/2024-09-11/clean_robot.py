"""
# Desafio

- Crie uma tabuleiro de Tamanho MxN, onde M e N são números inteiros positivos. 
- O tabuleiro deve ser preenchido com 0 para local vazio, -1 para lixo e 1 para obstaculos. 
- O robô deve começar na posição (X,Y) e deve se mover somente dentro do tabuleiro. 
- O robô deve se mover apenas na horizontal e vertical.
- O robô não ficar em cima de obstaculos.
- O robô só pode dar "um passo" por vez.
"""


from random import randint
from typing import Literal

VOID = 0
TRASH = 1
OBSTACLE = 7
ROBOT = 8

def gerenate_random_number(min: int, max: int) -> int:
    """
    Gerá um número aleatório entre min e max, considerando min e max como valores possíveis
    
    - Args:
        min::int: valor mínimo
        max::int: valor máximo
        
    - Returns:
        int: número aleatório
    """
    
    return randint(min, max)
    

def generate_board(m:int, n:int) -> list[list]:
    
    board = [[TRASH for i in range(0,n,1)] for j in range(0,m,1)]
    
    return board

def generate_position(board:list[list]) -> tuple[int, int]:
        
        width = len(board)
        height = len(board[0])
        
        x = gerenate_random_number(0, width - 1)
        y = gerenate_random_number(0, height - 1)
        
        return x, y

def place(board:list[list], x:int, y:int, type: Literal["obstacle", "robot"]) -> bool:
    
    width = len(board)
    height = len(board[0])
    
    result = True
    
    if x < 0 or x >= width or y < 0 or y >= height: # Checando se a posição é válida
        print("\nPosição inválida")
        result = False
    
    elif board[x][y] == OBSTACLE:
        print("\nJá existe um obstáculo nessa posição")
        result = False
        
    else:
        if type == "robot":
            board[x][y] = ROBOT
            print("\nRobô colocado com sucesso")
        elif type == "obstacle":
            board[x][y] = OBSTACLE
            print("\nObstáculo colocado com sucesso")
        else:
            raise ValueError("Tipo inválido")
    return result

def generate_obstacles(board:list[list], num_blocks:int) -> None:
    
    width = len(board)
    height = len(board[0])
    
    if num_blocks > width * height:
        raise ValueError("Número de obstáculos maior que o número de posições do tabuleiro")
    
    for _ in range(0,num_blocks,1):
        
        x, y = generate_position(board)
        
        while not place(board, x, y, 'obstacle'):
            x, y = generate_position(board)
            
def get_robot_position(board:list[list]) -> tuple[int, int]:
    
    width = len(board)
    height = len(board[0])
    
    for i in range(0,width,1):
        for j in range(0,height,1):
            if board[i][j] == ROBOT:
                return i, j
            
    raise ValueError("Robô não encontrado")
        
def move(board:list[list], x:int, y:int, direction: Literal["up", "down", "right", "left"]) -> bool:
    
    width = len(board)
    height = len(board[0])
    
    result = True
    
    oldx = x
    oldy = y
    
    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "right":
        y += 1
    elif direction == "left":
        y -= 1
    else:
        raise print("Direção inválida")
    
    if x < 0 or x >= width or y < 0 or y >= height: # Checando se a posição é válida
        print("\nPosição inválida")
        result = False
    
    elif board[x][y] == OBSTACLE:
        print("\nJá existe um obstáculo nessa posição")
        result = False
        
    else:
        board[x][y] = ROBOT
        board[oldx][oldy] = VOID
        print("\nRobô movido com sucesso")
        
    return result

def show_board(board:list[list]) -> None:
        
    for i in range(0,len(board),1):
        print(board[i])
        
def plot_board(board:list[list]) -> None:
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('TkAgg')
    plt.imshow(board, cmap='viridis', interpolation='none')
    plt.colorbar()  # Adiciona a barra de cores ao lado
    plt.title('Matriz')
    plt.show()

M = int(input("Digite o número de linhas do tabuleiro: "))
N = int(input("Digite o número de colunas do tabuleiro: "))

num_blocks = int(input("Digite o número de obstáculos: "))

x = int(input("Digite a posição inicial do robô (linha): "))
y = int(input("Digite a posição inicial do robô (coluna): "))

board = generate_board(M,N)

generate_obstacles(board, num_blocks)


while not place(board, x, y, 'robot'):
    x = int(input("Digite a posição inicial do robô (linha): "))
    y = int(input("Digite a posição inicial do robô (coluna): "))
    
show_board(board)

while True:
    direction = input("Digite a direção do movimento do robô: [up, down, right, left] ou 'exit' para sair: ")
    x,y = get_robot_position(board)
    
    if direction == "exit":
        break
    
    if move(board, x, y, direction):
        #show_board(board)
        plot_board(board)
    
    
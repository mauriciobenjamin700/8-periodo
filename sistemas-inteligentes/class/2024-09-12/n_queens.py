N = 8 # Tamanho do tabuleiro
QUEEN = 1 # Rainha
VOID = 0 # Espaço vazio
QUEEN_ICO = 'Q' # Ícone da rainha
VOID_ICO = '.' # Ícone do espaço vazio


def generate_board() -> list[list[int]]:
    # Define o tamanho do tabuleiro (8x8)
    
    board = [[VOID for _ in range(N)] for _ in range(N)]
    return board

def is_safe(board:list[list[int]], row:int, col:int) -> bool:
    """
    Confere se é seguro posicionar uma rainha na posição (row, col)
    
    - Args:
        - board::list[list[int]]: tabuleiro
        - row::int: linha
        - col::int: coluna
        
    - Returns:
        - bool: True se for seguro, False caso contrário
    """
   
    for i in range(0,col,1):  # Verifica a linha à esquerda, para ver se há uma rainha lá para matar a atual, percorrendo todos os elementos a esquerda da rainha
        if board[row][i] == QUEEN:
            return False

    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): # Verifica a diagonal superior à esquerda, percorrendo todas as linhas e colunas à esquerda da rainha
        if board[i][j] == 1:
            return False

    
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)): # Verifica a diagonal inferior à esquerda
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board:list[list[int]], col: int = 0) -> bool:
    """
    Resolve o problema das N rainhas
    
    - Args:
        - board::list[list[int]]: tabuleiro
        - col::int: coluna atual (Começamos da Coluna Zero)
        
    - Returns:
        - bool: True se a solução foi encontrada, False caso contrário
    """
    
    if col >= len(board): # Caso base: se todas as rainhas foram colocadas
        return True

    
    for i in range(0, len(board),1): # Tenta colocar uma rainha em cada linha da coluna atual
        
        if is_safe(board, i, col): # Coloca a rainha na posição (i, col) se for seguro colocala
            
            board[i][col] = QUEEN
            
            if solve_n_queens(board, col + 1): # Recursivamente tenta colocar o restante das rainhas
                return True

            # Se colocar a rainha na posição (i, col) não leva a uma solução,  remove a rainha

            board[i][col] = 0

    # Se a rainha não puder ser colocada em nenhuma linha da coluna atual, retorna False
    return False

def plot_board(board:list[list]) -> None:
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('TkAgg')
    plt.imshow(board, cmap='viridis', interpolation='none')
    plt.colorbar()  # Adiciona a barra de cores ao lado
    plt.title('Matriz')
    plt.show()

def print_board(board) -> None:
    for row in board:
        print(" ".join(QUEEN_ICO if x == QUEEN else VOID_ICO for x in row))

board = generate_board()

if solve_n_queens(board):
    #print_board(board)
    plot_board(board)
else:
    print("Solução não encontrada")
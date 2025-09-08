import random

# Constantes para estados do mar
marVazio = 0
MAR_NAVIO = 1
MAR_NAVIO_QUEBRADO = 2
MAR_ERRADO = 3

# Constantes visuais
CHAR_VAZIO = '~'
CHAR_NAVIO = '*'
CHAR_QUEBRADO = 'X'
CHAR_ERRADO = 'E'

# --- Funções ---
def inicializa_tabuleiro(linhas=10, colunas=10):
    #Cria tabuleiro vazio de tamanho linhas x colunas
    return [[marVazio 
             for _ in range(colunas)] 
             for _ in range(linhas)]

# Chamando a função e imprimindo o resultado
tabuleiro = inicializa_tabuleiro()
for linha in tabuleiro:
    print(linha)

'''
def mostrar_tabuleiro(tabuleiro, mostrar_navios=False):
    """Imprime o tabuleiro"""
    colunas = len(tabuleiro[0])
    print("   " + " ".join(f"{i:2}" for i in range(colunas)))
    print("  " + "---"*colunas)
    for i, linha in enumerate(tabuleiro):
        print(f"{i:2} ", end="")
        for cel in linha:
            if cel == MAR_VAZIO:
                print(f"{CHAR_VAZIO}  ", end="")
            elif cel == MAR_ERRADO:
                print(f"{CHAR_ERRADO}  ", end="")
            elif cel == MAR_NAVIO_QUEBRADO:
                print(f"{CHAR_QUEBRADO}  ", end="")
            elif cel == MAR_NAVIO:
                print(f"{CHAR_NAVIO if mostrar_navios else CHAR_VAZIO}  ", end="")
        print()

def ler_nome_jogador():
    nome = input("Jogador, digite seu nome: ").strip()
    return nome if nome else "Jogador"

def ler_posicao(mensagem="Digite linha,coluna: "):
    while True:
        try:
            linha, coluna = map(int, input(mensagem).split(","))
            return linha, coluna
        except:
            print("Entrada inválida! Use formato linha,coluna (ex: 2,3).")

def posicionar_barco(tabuleiro, qtd_navios=5):
    for i in range(qtd_navios):
        while True:
            x, y = ler_posicao(f"Digite posição do navio {i+1} (linha,coluna): ")
            if 0 <= x < len(tabuleiro) and 0 <= y < len(tabuleiro[0]):
                if tabuleiro[x][y] == MAR_VAZIO:
                    tabuleiro[x][y] = MAR_NAVIO
                    break
                else:
                    print("Já existe um navio aqui! Escolha outra posição.")
            else:
                print("Posição fora do tabuleiro!")

def atirar(tabuleiro, x, y):
    if tabuleiro[x][y] == MAR_NAVIO:
        tabuleiro[x][y] = MAR_NAVIO_QUEBRADO
        print("🎯 ACERTOU!")
        return True
    elif tabuleiro[x][y] == MAR_VAZIO:
        tabuleiro[x][y] = MAR_ERRADO
        print("💦 Água!")
        return False
    else:
        print("⚠️ Já atirou aqui!")
        return False

def contar_navios(tabuleiro):
    return sum(linha.count(MAR_NAVIO) for linha in tabuleiro)

# --- Jogo Principal ---
def batalha_naval():
    linhas, colunas = 10, 10
    navios_por_jogador = 5

    print("=== BATALHA NAVAL 10x10 ===")
    jogador = ler_nome_jogador()
    computador = "Computador"

    mar_jogador = inicializa_tabuleiro(linhas, colunas)
    mar_computador = inicializa_tabuleiro(linhas, colunas)

    # Posicionar navios
    print(f"\n{jogador}, posicione seus navios!")
    posicionar_barco(mar_jogador, navios_por_jogador)

    # Computador posiciona navios aleatoriamente
    for _ in range(navios_por_jogador):
        while True:
            x, y = random.randint(0, linhas-1), random.randint(0, colunas-1)
            if mar_computador[x][y] == MAR_VAZIO:
                mar_computador[x][y] = MAR_NAVIO
                break

    # Loop do jogo
    turno = 0
    while True:
        print("\nSeu tabuleiro:")
        mostrar_tabuleiro(mar_jogador, mostrar_navios=True)
        print("\nTabuleiro do computador:")
        mostrar_tabuleiro(mar_computador, mostrar_navios=False)

        if turno % 2 == 0:  # turno do jogador
            print(f"\n{jogador}, sua vez!")
            x, y = ler_posicao("Digite onde atirar (linha,coluna): ")
            atirar(mar_computador, x, y)
        else:  # turno do computador
            print(f"\n{computador} está atirando...")
            x, y = random.randint(0, linhas-1), random.randint(0, colunas-1)
            print(f"Computador atirou em ({x},{y})")
            atirar(mar_jogador, x, y)

        # Checar fim de jogo
        if contar_navios(mar_computador) == 0:
            print(f"\n🎉 {jogador} venceu! Todos navios inimigos afundados!")
            break
        elif contar_navios(mar_jogador) == 0:
            print(f"\n💀 {computador} venceu! Seus navios foram afundados...")
            break

        turno += 1

# Rodar jogo
if __name__ == "__main__":
    batalha_naval()
'''
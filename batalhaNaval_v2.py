tabuleiro = (10,10)  # (linhas, colunas)
linhas, colunas = tabuleiro

def criacao_tabuleiro():
# criação do tabuleiro 10x10
    mar = [["0" for _ in range(colunas)] #list comprehension
            for _ in range(linhas)]
    return mar #envia um valor da função de volta para quem chamou.

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
    # junta os elementos da linha separados por espaço
        print("|",",  ".join(linha), "|")  

# Criando e imprimindo o tabuleiro
#print(criacao_tabuleiro()) 

baseTabuleiro = criacao_tabuleiro()
imprimir_tabuleiro(baseTabuleiro)
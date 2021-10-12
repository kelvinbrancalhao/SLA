# Desafio de Matriz caracol, seja bem vindo:
print("Seja bem vindo ao desafio da Matriz Caracol:")
coluna = 0
linha = 0
max_coluna = int(input("Insira o número de colunas: "))
max_linha = int(input("Insira o numero de linhas: "))
numero = 0
direcionador_linha = 1
direcionador_coluna = 1
pos_linha = 0
pos_coluna = 0

def gerar_matriz (n_linhas, n_colunas):
    matriz = []

    for _ in range(n_linhas):
        matriz.append([" "] * n_colunas)

    return matriz

matriz_caracol = gerar_matriz(max_linha,max_coluna)

while max_coluna > 0:

    while pos_coluna < max_coluna:  #preenche as linhas
        numero += 1
        matriz_caracol[linha][coluna] = numero
        coluna = coluna + direcionador_coluna
        pos_coluna += 1

    pos_coluna = 0
    max_linha -= 1
    coluna = coluna - direcionador_coluna
    linha = linha + direcionador_linha

    while pos_linha < max_linha:
        numero += 1
        matriz_caracol[linha][coluna] = numero
        linha = linha + direcionador_linha
        pos_linha += 1

    pos_linha = 0
    max_coluna -= 1
    linha = linha - direcionador_linha
    coluna = coluna - direcionador_coluna
    direcionador_linha = direcionador_linha * -1
    direcionador_coluna = direcionador_coluna * -1

for row in matriz_caracol:
    print(row)
#programa finalizado!
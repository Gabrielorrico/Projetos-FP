import os; os.system('cls')

inimigos_tabuleiro = []
indices_inimigos_tabuleiros = []
inimigos_comestiveis = 0

tabuleiro = [["a8","b8","c8","d8","e8","f8","g8","h8"],["a7","b7","c7","d7","e7","f7","g7","h7"],["a6","b6","c6","d6","e6","f6","g6","h6"],["a5","b5","c5","d5","e5","f5","g5","h5"],["a4","b4","c4","d4","e4","f4","g4","h4"],["a3","b3","c3","d3","e3","f3","g3","h3"],["a2","b2","c2","d2","e2","f2","g2","h2"],["a1","b1","c1","d1","e1","f1","g1","h1"]]

def printar_tabuleiro(tabuleiro):
    for i in range (8):
        for j in range(8):
            print(f"{tabuleiro[i][j]:^8}", end = " ")
        print()
    return tabuleiro

def colocar_torre(posicao, adicionar):
    for i in range (8):
        for j in range(8):
            if tabuleiro[i][j] == posicao:
                tabuleiro[i][j] = adicionar
                coluna_torre = j
                linha_torre = i
    return coluna_torre, linha_torre

def colocar_inimigo(posicao_inimigo, adicionar_inimigo):
    for i in range (8):
        for j in range(8):
            if tabuleiro[i][j] != posicao:
                if tabuleiro[i][j] == posicao_inimigo:
                    tabuleiro[i][j] = adicionar_inimigo

                    

def verificar_inimigos_tabuleiro(adicionar_inimigo, tabuleiro):
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == adicionar_inimigo:
                indice_do_inimigo = i, j
                if indice_do_inimigo not in inimigos_tabuleiro:
                    inimigos_tabuleiro.append(indice_do_inimigo)


def verificar_comestiveis_torre(tabuleiro, linha_torre, coluna_torre, simbolo_inimigo):
    inimigos_comestiveis = []

    for i in range(linha_torre - 1, -1, -1):
        veri_coluna = tabuleiro[i][coluna_torre]
        if veri_coluna == simbolo_inimigo:
            indices_inimigos_tabuleiros.append((i, coluna_torre))
            inimigos_comestiveis.append((i, coluna_torre))
            break
        elif len(veri_coluna) == 1:
            break

    for i in range(linha_torre + 1, 8):
        veri_coluna = tabuleiro[i][coluna_torre]
        if veri_coluna == simbolo_inimigo:
            indices_inimigos_tabuleiros.append((i, coluna_torre))
            inimigos_comestiveis.append((i, coluna_torre))
            break
        elif len(veri_coluna) == 1:
            break

    for j in range(coluna_torre - 1, -1, -1):
        veri_linha = tabuleiro[linha_torre][j]
        if veri_linha == simbolo_inimigo:
            indices_inimigos_tabuleiros.append((linha_torre, j))
            inimigos_comestiveis.append((linha_torre, j))
            break
        elif len(veri_linha) == 1:
            break

    for j in range(coluna_torre + 1, 8):
        veri_linha = tabuleiro[linha_torre][j]
        if veri_linha == simbolo_inimigo:
            indices_inimigos_tabuleiros.append((linha_torre, j))
            inimigos_comestiveis.append((linha_torre, j))
            break
        elif len(veri_linha) == 1:
            break

    return inimigos_comestiveis


printar_tabuleiro(tabuleiro)


posicao = input("Insira a posição que deseja alterar: ")
adicionar = ("Torre")
qtd_inimigos = int(input("Quantos inimigos você vai adicionar? "))

for i in range(qtd_inimigos):
    posicao_inimigo = input("Insira a posição do inimigo: ")
    adicionar_inimigo = ("Peão")
    colocar_inimigo(posicao_inimigo, adicionar_inimigo)
    verificar_inimigos_tabuleiro(adicionar_inimigo, tabuleiro)

coluna_torre, linha_torre = colocar_torre(posicao, adicionar)

comestiveis = verificar_comestiveis_torre(tabuleiro, linha_torre, coluna_torre, adicionar_inimigo)

print("\n")
print(inimigos_tabuleiro)
print(indices_inimigos_tabuleiros)
print(f"Quantidade de inimigos no tabuleiro: {len(inimigos_tabuleiro)}")
print(f"Quantidade de inimigos comestíveis: {len(comestiveis)}")
print("\n")
printar_tabuleiro(tabuleiro)
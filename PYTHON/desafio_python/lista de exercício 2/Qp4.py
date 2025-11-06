import os; os.system('cls')

matriz = [[],[],[]]

colun = int(input("Digite em qual coluna você deseja realizar a operação: (de 0 a 2): "))
operacao = input("Digite a operação que você deseja realizar:\n[S] - SOMA\n[P] - PRODUTO\nOperação: ")


for i in range(3):
    for j in range (3):
        valor = int(input(f"Digite os valores da posição[{i}][{j}]: "))
        matriz[i].append(valor)

soma_coluna = 0
mult_coluna = 1

for i in range(3):
    for j in range (3):
        print(f"{matriz[i][j]:^4}", end = " ")
        if colun == j:
            if operacao == 'S':
                soma_coluna += matriz[i][j]
            elif operacao == 'P': 
                mult_coluna *= matriz[i][j]
    print()

if soma_coluna == 0:
    print("Coluna escolhida não existe!")
else:
    if operacao == 'S':
        print(f"A soma da coluna {colun} é: {soma_coluna}")
    elif operacao == 'P':
        print(f"A multiplicação da coluna {colun} é: {mult_coluna}")



    



        
        
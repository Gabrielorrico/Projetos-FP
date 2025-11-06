import os; os.system('cls')

matriz = [[],[],[]]

soma_impares = 0
soma_coluna = 0

        

for i in range (3):
    for j in range(3):
        numeros = int(input(f"Digite os numeros nas posições {i}x{j}: "))
        matriz[i].append(numeros)

      
menor_valor = 1000000000000000000000000

for i in range (3):
    for j in range(3):

        if matriz[i][j]%2 != 0:
            soma_impares += matriz[i][j]

        if j == 0:
            soma_coluna += matriz[i][j]

        if matriz[2][j] < menor_valor:
            menor_valor = matriz[2][j]

for i in range (3):
    for j in range(3):
        print(f"{matriz[i][j]:^4}", end = " ")
    print("")
        


print(soma_impares, soma_coluna, menor_valor)
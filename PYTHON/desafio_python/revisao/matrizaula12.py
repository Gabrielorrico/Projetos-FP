import os; os.system('cls')

matriz = [[],[],[]]

produto_diagonal = 1
soma = 0
soma_coluna = 0



for i in range (3):
    for j in range (3):
        valores = int(input(f"Digite os valores na posição {i}x{j}: "))
        matriz[i].append(valores)
        soma += matriz[i][j]
        media = soma/9
    
        if i == j:
            produto_diagonal *= matriz[i][j]

        if j == 1:
            soma_coluna += matriz[i][j]

numeros_menores = []

for i in range (3):
    for j in range (3): 
        if matriz[i][j] <= media:
            
            menor = matriz[i][j]
            numeros_menores.append(menor)


for i in range (3):
    for j in range (3):
        print(f"{matriz[i][j]:^4}",end = " ")

    print("")


print(produto_diagonal)
print("média: ", media)
print("Soma segunda coluna: ", soma_coluna)
print(numeros_menores)


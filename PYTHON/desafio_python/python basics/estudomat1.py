import os; os.system('cls')

matriz = [[],[],[]]

for i in range (3):
    for j in range (3):
        valor = int(input(f"Digite os elementos[{i}][{j}]: "))
        matriz[i].append(valor)

multiplicacao = 1
cont = soma_todos = 0
maior_valor = 0

for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]:^4}", end = " ")
        soma_todos += matriz[i][j]
        cont +=1

        if i == j:
            multiplicacao *= matriz[i][j]
        
        if matriz[i][1] > maior_valor:
            maior_valor =  matriz[i][1]
    print()

media = soma_todos / cont

menor_media = []

for i in range(3):
    for j in range(3):
        if matriz[i][j] <= media:
            menor_media.append(matriz[i][j])
    print()


print(f"O produto da diagonal principal é: {multiplicacao}")
print(f"A média dos valores é: {media}")
print(f"O Maior valor é: {maior_valor}")
print(f"Os valores menores ou iguais a média são {menor_media}")


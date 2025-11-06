import os; os.system('cls')

i = 0
carromaisantig = 9999
carromaisnovo = 0


while True:
    i += 1
    marca = input(f"Digite a marca do {i}° veículo: ")
    anolanc = int(input(f"Digite o ano de lançamento do {i}° veículo: "))
    


    if anolanc > carromaisnovo:
        carromaisnovo = anolanc

    if anolanc < carromaisantig:
        carromaisantig = anolanc

    continuar = input(f"Você deseja continuar? ")
    if continuar == "não":
        break

    

print("As informações dos carros cadastrados é: ")
print(f"A quantidade de carros cadastrados é: {i} \nO carro mais novo é do ano: {carromaisnovo} \nO carro mais antigo é: {carromaisantig} ")


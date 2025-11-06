import os;os.system('cls')

preco_duvida = 40

idade = int(input("Digite sua idade: "))
sit = input("Você é estudante? (digite S para SIM e N para não)")
horario = int(input("Digite o horario?"))

if sit == 'S':
    preco_duvida = preco_duvida * 0.5
    print(f"O preço final é de {preco_duvida}")

elif idade >= 60:
    preco_duvida = preco_duvida * 0.7
    print(f"O preço final é de {preco_duvida}")

elif horario >=6 and horario <= 22:
    print(f"O preço final é de {preco_duvida}")

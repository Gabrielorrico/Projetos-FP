import os; os.system('cls')

t = 0
b = 0
bt = 0
out = 0

for i in range (5):
    print("Escreva qual o serviço realiado no pet: ")
    a = int(input("[1] - banho \n[2] - tosa \n[3] - banho e tosa \n[4] - outros \n"))

    if a == 1:
        b += 1
    elif a == 2:
        t += 1
    elif a == 3:
        bt += 1
    elif a == 4:
        out += 1
    else: 
        print(" o numéro inserido está fora das opções possíveis \n ")

print(f"A quantidade de banhos é: {b}\n A quantidade de tosas é: {t}\n A quantidade de banhos e tosas é: {bt}\n A quantidade de outros é: {b}")

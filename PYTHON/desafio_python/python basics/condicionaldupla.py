import os; os.system('cls')

anoadm = int(input("Digite o ano de admissão: "))
anoreajuste = int(input("Digite o ano do ultimo reajuste salarial: "))
salarioatual = float(input("Digite seu salario atual: "))

tempotrabalho = 2025 - anoadm

if anoreajuste - anoadm >= 2: 
    if tempotrabalho > 10:
        print("O seu novo salário é de: ", salarioatual * 1.3)
    elif tempotrabalho >= 5 and tempotrabalho <=10:
        print("O seu salário atual é de: ", salarioatual * 1.2)
    elif tempotrabalho < 5 and tempotrabalho > 1:
        print("O seu novo salário é  de: ", salarioatual * 1.10)
else:
    print("você não está apto a receber aumento!")

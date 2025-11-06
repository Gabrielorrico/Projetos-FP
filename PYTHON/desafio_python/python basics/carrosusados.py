import os
os.system("cls")

qntcarros = int(input("Digite a quantidade de carros vendidos: "))
valortotvend = float(input("digite o valor total dos carros vendidos: "))
salariofixo = float(input("Digite o salario fixo que você recebe: "))
comifixa = float(input("digite a comissão fixa por carro: "))

salariotot = qntcarros * comifixa + salariofixo + valortotvend * 0.05

print(f"O salario total desse mês é de {salariotot}")
 

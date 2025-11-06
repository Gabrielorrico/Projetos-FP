import os; os.system('cls')

soma = 0

while True:
    valorprod = float(input(f"Digite o valor dos produtos ou 0 para terminar o programa:  "))
    
    if valorprod > 0:
        soma = soma + valorprod

    elif valorprod == 0:
        break

if soma > 1000:
    soma = soma * 0.9

print(f"\nO valor total a pagar é R${soma} ")


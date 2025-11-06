import os; os.system("cls")
print("---------VERIFICADOR DE NÚMERO PERFEITO---------")

num1 = int(input("Digite o número: "))
numdiv = num1 // 2
soma=0

for i in range (1, numdiv ):

    if num1 % i == 0:
        soma = soma + i

if soma == numdiv:
    print("O número é perfeito!")

else:
    print("O número não é perfeito ")



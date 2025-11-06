import os; os.system("cls")

numvisi = int(input("Digite o número de visitantes "))
alturaMin = float(input("\nDigite a altura mínima "))
alturaMax = float(input("\nDigite a altura máxima "))
podeentrar = 0
naopodeentr = 0

for i in range (numvisi):
    alturavisi = float(input(f"Digite a altura do {i+1}°: "))

    if alturavisi >= alturaMin and alturavisi <= alturaMax:
        print("Acesso permitido!\n")
        podeentrar += 1
    else: 
        print("Acesso negado!\n")
        naopodeentr += 1

print(f"O número de vistantes que pode entrar é: {podeentrar} \nO número de pessoas que não pode entrar é: {naopodeentr}")




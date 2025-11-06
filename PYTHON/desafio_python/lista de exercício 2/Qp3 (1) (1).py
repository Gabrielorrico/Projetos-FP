import os; os.system('cls')

matriz = []

tempo_min = []
valor_hora = []
salarios = []
profissoes = ["Desenvolvedor python","Cientista de dados","analista QA"]

for i in range (3):
    print(profissoes[i])
    slr = float(input("Digite o seu salario médio: "))
    salarios.append(slr)
    exp = int(input("Digite o tempo de experiencia mínimo em anos: "))
    tempo_min.append(exp)
    vh = float(input("Digite o valor recebido por hora trabalhada: "))
    valor_hora.append(vh)
matriz.append(salarios)
matriz.append(tempo_min)
matriz.append(valor_hora)
    
soma_diagonal = 0
media_salario = 0
print("\nSalarios:\tExperiencia minima:\t     Valor hora:")

soma = 0
#minhas lihas viraram colunas nesse proximo for 
for j in range (3):
    soma = soma + matriz[0][j]
    for i in range (3):
        print(f"{matriz[i][j]:^5}", end = '\t\t\t')
        if j == i:
            soma_diagonal += matriz[i][j]
        



    print()


print(f"A média salarial das 3 profissões é: {soma / 3:.2f}")
print(f"A soma da diagonal principal é: {soma_diagonal} ")





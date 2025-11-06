import os; os.system('cls')

nomes_comp = []
idades = []

min_tenta = 0
qtdaptos = int(input("Digite a quantidade de funcionarios aptos a se aposentar: "))

while min_tenta < qtdaptos:
    
    nomes = (input(f"\nDigite o nome do funcionario: ")) 
    idade = int(input(f"Digite a idade do funcionario: "))

    if idade < 60:
        print("\nO funcionario ainda não está apto a se aposentar!")

    else:
        min_tenta += 1
        nomes_comp.append(nomes)
        idades.append(idade)

mais_idoso = max(idades)
mais_idoso_index = idades.index(mais_idoso)
nome_mais_idoso = nomes_comp[mais_idoso_index]
media_idades = sum(idades) / len(idades)

print("Funcionarios a se aposentar em 2025")
print("*"*35)
for i in range (len(idades)):
    print(f"Nome: {nomes_comp[i]}\t\t\t Idade: {idades[i]} anos")

print(f"Funcionario mais antigo: {nome_mais_idoso}")
print(f"Média das idades: {media_idades}")


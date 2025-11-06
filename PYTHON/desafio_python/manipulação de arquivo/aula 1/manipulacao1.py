import os; os.system('cls')

arquivo1 = open("arquivo1.txt","w", encoding = "utf8")

nomes = []
sobrenomes = []
idades = []

qtd_pessoas = int(input("Digite a quantidade de pessoas: "))

for i in range(qtd_pessoas):
    nome = input("Digite seu nome: ")
    nomes.append(nome)
    sobrenome = input("Digite seu sobre-nome")
    sobrenomes.append(sobrenome)
    idade = input("Digite sua idade: ")
    idades.append(idade)

arquivo1.writelines("Há " + str(qtd_pessoas) + " pessoas cadastradas" +"\n")

for i in range (qtd_pessoas):
    qtd_pessoas = str(qtd_pessoas)
    arquivo1.writelines("Nome: " + nomes[i] +" " + sobrenomes[i] + " " +"Idade: "+ idades[i] + "\n")

arquivo1.close()





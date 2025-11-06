import os; os.system('cls')
arquivo = open("arquivo.txt", "w", encoding= "utf8")

nomes = []
racas = []


for i in range (5):
    nome = input("Digite o nome do cachorro: ")
    nomes.append(nome)
    raca = input("Digite a raça dos cachorros: ")
    racas.append(raca)


for i in range (5):
    arquivo.writelines(" Nome: " + nomes[i] +" Raça: " + racas[i] + "\n")



arquivo.close()

arquivo = open("arquivo.txt", "r", encoding= "utf8")

print(arquivo.read())

arquivo.close()
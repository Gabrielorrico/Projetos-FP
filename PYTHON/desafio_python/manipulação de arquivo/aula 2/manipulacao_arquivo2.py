import os; os.system('cls')

file = open("file2.txt", "w")

def comparacao(votos,cont_sushi,cont_churras):
    cont_sushi = votos.count("1")
    cont_churras = votos.count("2")

    if cont_sushi == cont_churras:
        print("empate")
    elif cont_sushi > cont_churras:
        print("sushi ganhou")
    elif cont_churras > cont_sushi:
        print("churras ganhou")

    return cont_churras,cont_sushi 

for i in range(10):
    voto = input("Digite seu voto: ")
    file.write(voto + "\n")

file.close()

votos = []

file = open("file2.txt","r")

for linha in file:
    votos.append(linha.strip())

file.close()

sushi = 0
churrasco = 0

comparacao(votos,sushi,churrasco)
    

print(votos)


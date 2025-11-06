import os; os.system('cls')

votos = []

votadores = int(input("Digite a quantidade de votos: "))

for i in range(votadores):
    print("Escolha seu candidato")
    voto = int(input("Escolha 1 para A ou 2 para B"))
    if voto == 1 or voto == 2:
        votos.append(voto)
    else: 
        print("Insira um valor válido")


votos1 = votos.count(1)
votos2 = votos.count(2)
valor_tot = len(votos)
prc1 = (votos1/valor_tot) * 100
prc2 = (votos2/valor_tot) * 100

if votos1 > votos2:
    print("\nO candidato A ganhou!")
    print(f"A porcentagem de votos do candidato A é: {prc1}%")

elif votos2 > votos1: 
    print("\nO candidato B venceu")
    print(f"A porcentagem de votos do candidato B é: {prc2}%")
else: 
    print("A votação deu empate!")
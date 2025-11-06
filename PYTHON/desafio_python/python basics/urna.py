import os; os.system("cls")
print("----------------URNA ELETRONICA----------------")
print("\n1. [Harry Potter] \n2. [Hermione Granger] \n3. [Branco] \n4. [Encerrar]")
harry = 0
hermione = 0
branco = 0 


while True:
    voto = int(input("\nDigite o seu voto: "))

    if voto == 1:
        harry += 1
    elif voto == 2:
        hermione += 1
    elif voto == 3:
        branco += 1
    elif voto == 4:
        break
    else:
        print("voto inválido")

print("A quantidade de votos é:")
print(f"Harry: {harry} \nHermione: {hermione} \nBranco: {branco}")






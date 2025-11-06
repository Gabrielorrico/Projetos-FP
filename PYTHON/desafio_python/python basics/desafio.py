import os; os.system('cls')


vot = []
quantidadetot = 0
campeao = ""

while True:
    votos = int(input("Dgite seu voto de 7 à 11: "))

    if votos == 0:
        break

    elif votos >= 7 and votos <= 11:
        vot.append(votos)

    else: 
        print("O número está fora do intervalo")

contadordo7 = vot.count(7)
contadordo8 = vot.count(8)
contadordo9 = vot.count(9)
contadordo10 = vot.count(10)
contadordo11 = vot.count(11)
cont = [contadordo7, contadordo8, contadordo9, contadordo10, contadordo11,] 

if max(cont) == contadordo7:
    campeao = "o camisa 7 "
elif max(cont) == contadordo8:
    campeao = "o camisa 8"
elif max(cont) == contadordo9:
    campeao = "o camisa 9"
elif max(cont) == contadordo10:
    campeao = "o camisa 10"
elif max(cont) == contadordo11:
    campeao = "o camisa 11"



quantidadetot = contadordo7 + contadordo8 + contadordo9 + contadordo10 + contadordo11




print("\nO número de votos de cada participante em porcentagem é: \n")
print(f"Votos do Camisa 7: {((contadordo7 / quantidadetot)* 100):.2f}% \nVotos do camisa 8: {((contadordo8 / quantidadetot)* 100):.2f}% \nVotos do camisa 9: {((contadordo9 / quantidadetot) * 100):.2f}% \nVotos do camisa 10: {((contadordo10 / quantidadetot) * 100):.2f}% \nVotos do camisa 11: {((contadordo11 / quantidadetot) * 100):.2f}% ")
print(f"O campeão foi {campeao} ")



    


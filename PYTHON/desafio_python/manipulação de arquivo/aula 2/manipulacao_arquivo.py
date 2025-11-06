import os; os.system('cls')

numero_aumentadas = 0
file = open("file.txt","w")

for i in range(3):
    valor = input("Digite o número: ")
    file.write(valor + "\n")
    
file.close()

file = open("file.txt","r")

espaco_amostral = []
for linha in file:
    espaco_amostral.append(int(linha.strip()))
    
file.close()

qtd_aumentos = 0
for i in range(1, len(espaco_amostral)):
    if espaco_amostral[i] > espaco_amostral[i - 1]:
        qtd_aumentos += 1
print(espaco_amostral)
print(qtd_aumentos)







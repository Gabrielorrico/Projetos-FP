import os 
os.system("cls")

qntmed = int(input("Digite a quantidade média de cigarros fumados por dia: "))
qntanos = int(input("Digite a quantos anos você fuma: "))

qntcigarros = qntmed * (365 * qntanos)

tempoperdido = qntcigarros * (10/60)/24

print("A quantidade de dias perdidos até o momento foi de: ", tempoperdido," Dias")
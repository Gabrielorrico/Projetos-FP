import os; os.system('cls')

frase = input("Digite a frase: ")
palavra_substituir = input("Digite a palavra que quer substituir: ")
palavra_troca = input("Digite a  nova palavra: ")

print(f"Frase antes: {frase}")

if palavra_substituir in frase:
    frase = frase.replace(palavra_substituir, palavra_troca)
    print(frase.upper())
else: 
    print(" A palavra não está na frase")
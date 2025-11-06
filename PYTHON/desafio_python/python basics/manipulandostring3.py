import os; os.system('cls')

frase_qualquer = input("Digite a sua frase: ")

frase1_sem_espaco = frase_qualquer.replace(" ", "").upper()


if frase1_sem_espaco[::-1 ]== frase1_sem_espaco:
    print("A frase é um palindromo")
else:
    print("Não é um palindromo")



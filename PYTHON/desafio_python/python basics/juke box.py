import os; os.system('cls')

print(" Escolha dois números somados que dem o indice da música escolhida abaixo \
       \n [0] CHEIA DE MANIAS \n [1] ME LEVA JUNTO COM VOCÊ \n [2] É TARDE DEMAIS \n \
[3] QUANDO TE ENCONTREI \n [4] DEUS ME LIVRE \n [5] CIÚME DE VOCÊ \n [6] CIGANA ")

a = int(input("Digite o primeiro número de 0 a 6: "))

b = int(input("Digite o segundo número de 0 a 6: "))

soma = a + b

if (soma == 0):
    print("Play Cheia de manias")

elif(soma == 1):
    print("play Me leva junto com você")

elif(soma == 2):
    print("play É tarde demais")

elif(soma == 3):
    print("play Quando te encontrei")

elif(soma == 4):
    print("play Deus me livre")

elif(soma == 5):
    print("play Ciúme de você")

elif(soma == 6):
    print("play Cigana")

else: 
    print("a soma está fora do intervalo; tente novamente!")


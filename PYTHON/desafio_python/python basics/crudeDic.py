import os; os.system('cls')

cardapio =  {"Coxinha":[5.00], "Pastel": [4.00], "Suco": [3.50], "Bolo": [4.50]}

print("\n",cardapio)

while True:
    escolha = input("Você deseja remover, adcionar ou modificar o valor de um produto do cardápio? (SIM/NÃO)")
    

    if escolha == "NÃO":
        print(cardapio)
        break

    elif escolha == "SIM":
        tipo_escolha = int(input("[1] - remover\n[2] - adcionar\n[3] - modificar\nESCOLHA: "))

        if tipo_escolha == 1:
            escolha_remover = input("Digite o nome do que você quer apagar: ")
            print(cardapio.pop(f"{escolha_remover}","Não encontrado"))

        elif tipo_escolha == 2:
            escolha_adcionar = input("Digite o nome do que vocé quer adcionar: ")
            preco = int(input("Digite o preço do produto: "))

            cardapio[escolha_adcionar] = preco

        elif tipo_escolha == 3:
            escolha_mudar = input("Escolha o nome do produto que você quer mudar o preço: ")
            novo_valor = int(input("Digite o novo valor do produto: "))

            cardapio[escolha_mudar] = novo_valor
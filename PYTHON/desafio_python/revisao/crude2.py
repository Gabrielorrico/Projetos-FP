import os; os.system('cls')

nomes = []

while True:
    opcoes = int(input("Escolha dentre as opções abaixo:\n[1] - Adicionar nome a uma lista\n[2] - Exibir os nomes da lista\n[3] - Substituir o nome na lista\n[4] - Deleta o nome na lista\n[5] - Encerra o código\nEscolha: "))

    if opcoes == 1:
        nome = input("Digite o nome que você quer adicionar: ")
        nomes.append(nome)

    elif opcoes == 2:
        for i in range (len(nomes)):
            print(f"{i} - {nomes[i]}")

    elif opcoes == 3: 
        for i in range (len(nomes)):
            print(f"{i} - {nomes[i]}")

        indice = int(input("Digite o indice do nome que você quer apagar: "))

        if indice >= 0 and indice < len(nomes):
            novo_nome = input("Digite o novo nome: ")
            nomes[indice] = novo_nome
        else: 
            print("esse indice não existe na lista! ")

    elif opcoes == 4:

        indice = int(input("Digite o indice do nome que você quer apagar: "))

        if indice >= 0 and indice < len(nomes):
            nomes.pop(indice)
            
        else: 
            print("esse indice não existe na lista! ")

    elif opcoes == 5: 
        print("Fim do código")
        break




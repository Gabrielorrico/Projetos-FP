import os; os.system('cls')

nomes = []

while True:
    opcoes = int(input("Escolha dentre as opções abaixo:\n[1] - Adicionar nome a uma lista\n[2] - Exibir os nomes da lista\n[3] - Substituir o nome na lista\n[4] - Deleta o nome na lista\n[5] - Encerra o código\nEscolha: "))

    if opcoes == 5:
        break

    elif opcoes == 1:
        nome = input("Digite o nome que você deseja adcionar a lista: ")
        nomes.append(nome)
    
    elif opcoes == 2:
        for i in range (len(nomes)):
            print(f"{i} - {nomes[i]}")

    elif opcoes == 3:
        for i in range (len(nomes)):
            print(f"{i} - {nomes[i]}")

        indice_nome = int(input("\nDigite o indice do nome que você quer substituir: "))

        if indice_nome >= 0 and indice_nome <= len(nomes):
            novo_nome = input("Digite o novo nome: ")
            nomes[indice_nome] = novo_nome

    elif opcoes == 4:
        for i in range (len(nomes)):
            print(f"{i} - {nomes[i]} ")

        indice_nome = int(input("\nDigite o indice do nome que você quer deletar: "))
        if indice_nome >= 0 and indice_nome <= len(nomes):
            nomes.pop(indice_nome)
        else:
            print("O indice escolhido não faz parte do vetor")
            
        



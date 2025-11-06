import os; os.system("cls")

nome = []
i=0

while True:
    acao = input(("Escolha a função que você deseja: \n[1] Create\n[2] Read\n[3] Update\n[4] Delete\n[5] Encerrar\n"))
    
    if acao == '5':
        break
    elif acao == '1':
        nome.append(input("Digite o nome a ser adicionado na lista: "))
    elif acao == '2':
        for i in range (len(nome)) :
          print(f"posicao {i}, nome {nome[i]}")
    elif acao == '3':
        procura =int(input("Qual o índice do nome que você quer mudar? "))
        if procura >= 0 and procura <= len(nome):
            novoN = input("Digite o novo nome: ")
            nome[procura] = novoN
        else:
            print("O índice não corresponde a nenhum valor na lista!")
    elif acao == '4':
        procura = int(input("Qual o índice do nome que você quer remover? "))
        if procura >= 0 and procura <= len(nome):
            nome.pop(procura)
        else:
            print("O índice digitado não corresponde a nenhum nome na lista!")
import os; os.system('cls')
matriz = []

qtd_alunos = int(input("Digite a quantidade de alunos: "))
qtd_notas = int(input("Digite a quantidade de notas: "))

for i in range (qtd_alunos):
    linha = []
    for j in range (qtd_notas):
        nota = float(input("Digite as notas dos 3 alunos: "))
        linha.append(nota)
    matriz.append(linha)

for linha in matriz : 
    for coluna  in linha :
        print(matriz[i][j],end= "\t")
    print()
    

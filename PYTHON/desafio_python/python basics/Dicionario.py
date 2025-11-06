import os; os.system('cls')
dic = {}

qtd_num = int(input("Digite um número: "))

for i in range (qtd_num):
    dic[i] = i**2

print(dic)
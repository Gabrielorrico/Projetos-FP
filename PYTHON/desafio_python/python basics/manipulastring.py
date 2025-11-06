import os; os.system('cls')
teste = "Sorria hoje é quinta" 

#mostra o intervalo desejado 
print(teste[0:6])
#o dois significa de dois em dois caracteres
print(teste[0:6:2])
#print a quantidade de caracteres com len
print(len(teste))

for i in range (len(teste)):
    for j in range (len(teste)):
        print(teste[i], end = " ") 
    print() 
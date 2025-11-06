import os; os.system('cls')

mouse = []

qtd = int(input("digite a quantidade de mouses: "))

for i in range (qtd):
    print("----------QUAL A SITUAÇÃO DO MOUSE?----------")

    sitmouse = int(input("[1] Necessita da esfera\n[2] Necessita de limpeza \n[3] Necessita troca de cabo ou conector\n[4] Quebrado ou inutilizado\n:"))
    

    if sitmouse >= 1 and sitmouse <= 4:
        mouse.append(sitmouse)
    else: 
        print("Opção inválida")

esfera = mouse.count(1)
limpeza = mouse.count(2)
troca = mouse.count(3)
quebrado = mouse.count(4)

print("*"*76)
print(f"Quantidade de mouses:  {len(mouse)}\n")
print("Situação\t\t\t Quantidade\t\t\t Percentual")
print(f"1 - Necessita de esfera:\t\t{esfera}\t\t\t {(esfera/len(mouse))*100:.2f}%")
print(f"2 - Necessita de limpeza:\t\t{limpeza}\t\t\t {(limpeza/len(mouse))*100:.2f}%")
print(f"2 - Necessita de troca de cabo:\t\t{troca}\t\t\t {(troca/len(mouse))*100:.2f}%")
print(f"2 - quebrado ou inutilizado:\t\t{quebrado}\t\t\t {(quebrado/len(mouse))*100:.2f}%")
import os ; os.system('cls')

lados = []
i = 0

for i in range (3):
    i += 1
    lado = int(input(f"Digite o lado do {i}° triangulo: "))
    lados.append(lado)

lado1 = lados[0]
lado2 = lados[1]
lado3 = lados[2]

if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2: 
   print("O triangulo não é existente!")   

else:
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print("O trinagulo é equilátero!")  
        
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triango é isoceles!")

    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("O triangulo é escaleno") 
    


 



print(lado1, lado2, lado3)
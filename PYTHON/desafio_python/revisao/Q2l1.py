import os; os.system('cls')

conversao = input("Digite para qual temperatura você deseja converter:\n[C] - celsius\n[F] - farenheit\nQual: ")
temperatura = int(input("Digite a temperatura que voce deseja converter: "))

if conversao == 'F' or conversao == 'f':
    temp_final = (temperatura * 9/5) + 32
    print(f"A temperatura convertida para Celsius é: {temp_final:.2f} °F")

elif conversao == 'C' or conversao == 'c':
    temp_final = (temperatura - 32) * 5/9
    print(f"A temperatura convertida para Farenheit é: {temp_final:.2f} °C")

else: 
    print("A opção escolhida não é válida!")



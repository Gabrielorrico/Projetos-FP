import os; os.system('cls')

level = int(input(" BIU! digite o level do voltorb: "))

if level > 0 and level < 21 : 
    print(" A pontência do choque foi de: ", 20 + level ** 3," WATTS")
elif level >= 21 and level < 41:
    print(" A pontência do choque foi de: ", 8000 + (level - 10) ** 2, "WATTS")
elif level >= 41 and level < 61: 
    print(" A pontência do choque foi de: ", 9000 + level * 5, "WATTS")
elif level >= 61 and level < 81: 
    print(" A pontência do choque foi de: ", 9300 + level * 2, "WATTS")
elif level >= 81 and level <= 100:
    print(" A pontência do choque foi de: ", 9500 + level , "WATTS")
else: 
    print("O valor informado não está dentro do intervalo de 1 a 100")

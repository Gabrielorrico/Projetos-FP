import os; os.system('cls')

vot = int(input("Digite o número total de votos: "))
candA = 0
candB = 0



for i in range (vot):
   print("Vote no seu candidato")
   cand = int(input("[1]. para candidato A e [2]. para candidato B: "))
   
   if cand == 1:
      candA += 1
   elif cand == 2:
      candB += 1 

soma = candA + candB

if candA > candB:
   print("\nO candidato A ganhou!")
   print(f"A porcentagem de votos do candidato A é  {(candA/soma)*100}% ")
elif candB > candA: 
   print("\nO candidato B ganhou!")
   print(f"A porcentagem de votos do candidato B é  {(candB/soma)*100}% ")
else:
   print("\nA votação empatou!")




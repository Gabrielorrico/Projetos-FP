import os; os.system('cls')

escolhas = []
invalidos = 0

for i in range (10):
    print("*"*40)
    print("[1] - Romance\n[2] - Ficção\n[3] - Mistério\n[4]- Não ficção")
    votos = int(input("Digite o seu voto: "))

    if votos >= 1 and votos <= 4:
        escolhas.append(votos)

    else: 
        invalidos += 1

romance = escolhas.count(1)
ficcao = escolhas.count(2)
misterio = escolhas.count(3)
nao_ficcao = escolhas.count(4)

print("*"*60)
print("O número total de votos para cada genero: ")
print(f"[1] - Romance: {romance}\n[2] - Ficção: {ficcao}\n[3] - Mistério: {misterio}\n[4]- Não ficção: {nao_ficcao}")
print(f"A quntidade de votos inválidos é: {invalidos}")

if romance > ficcao and romance > misterio and romance > nao_ficcao:
    print('Romance foi o mais votado!')
elif ficcao > romance and ficcao > misterio and romance > nao_ficcao:
    print('Ficcao foi o mais votado!')
elif misterio > romance and misterio > ficcao and misterio > nao_ficcao:
    print('Misterio foi o mais votado!')
elif nao_ficcao > romance and nao_ficcao > ficcao and nao_ficcao > misterio:
    print('Não Ficção goi o mais votado!')
else: 
    print('Empate')

if len(escolhas) == romance:
    print("O gênero campeão foi romance")

elif max(escolhas) == ficcao:
    print("O gênero campeão foi Ficção")

elif max(escolhas) == misterio:
    print("O gênero campeão foi Mistério")

elif max(escolhas) == nao_ficcao:
    print("O gênero campeão foi Não-Ficção")

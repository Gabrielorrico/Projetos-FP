import os; os.system('cls')

media_maior7 = []
media_menor = []
nome = []
maior_media = 0

for i in range (5):
    nomes = input(f"Digite o nome da {i+1}° escola: ")
    nome.append(nomes)
    medias = float(input(f"Digite a media da {i+1}° escola: "))

    if medias > 7 and medias <= 10:
        media_maior7.append(medias)

    elif medias <= 7 and medias >= 0:
        media_menor.append(medias)

maior_media = max(media_maior7)
indice_maior_media = media_maior7.index(maior_media)
qtd_total = len(media_maior7)

print(f"A quantidade de escolas com media superior a 7 é: {qtd_total}")
print(f"A soma total das medias das escolas é: {sum(media_maior7)+ sum(media_menor)}")
print(f"A escola com maior média é:  [{nome[indice_maior_media]}] com média igual a: {maior_media}")
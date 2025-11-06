import os
os.system("cls")

distancia = float(input("Digite a distancia total da viagem: "))
velocidadem = float(input("Digite a velocidade média: "))
consumo = float(input("Digite o consumo médio de combustivel do veículo (em km/l): "))
precoL = float(input("Digite o preço do litro de combustivel: "))

tempoestim = distancia/ velocidadem
quantcons = distancia / consumo 
custotot = quantcons * precoL

print(f"O tempo estimado da viagem foi de {tempoestim} horas\n A quantidade total de combustível necessária {quantcons}\n O custo total estimado da viagem {custotot}")
distancia = float(input("digite a distância da viagem em km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print (f"o preço da passagem é: R${preco: .2f}")
kwh_consumidos = float(input("digite a quantidade de kwh consumida: "))
tipodeinstalacao = input("digite o tipo de instalação (R para residências, I para industrias, C para comércios): ")

if tipodeinstalacao == 'R' or tipodeinstalacao == 'r':
    if kwh_consumidos <= 500:
        preco = kwh_consumidos * 0.40
    else:
        preco = kwh_consumidos * 0.65
elif tipodeinstalacao == 'I' or tipodeinstalacao == 'i':
    if kwh_consumidos <= 1000:
        preco = kwh_consumidos * 0.55
    else:
        preco = kwh_consumidos * 0.60
elif tipodeinstalacao == 'C' or tipodeinstalacao == 'c':
    if kwh_consumidos <= 1200:
        preco = kwh_consumidos * 0.55
    else:
        preco = kwh_consumidos * 0.60
else:
    print("não existe essa instalação amigo. use R para residências, I para indústrias e C para comércios.")

print(f"O preço a pagar é: R${preco:.2f}")
  
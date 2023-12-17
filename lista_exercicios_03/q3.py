soma = 0
quantidade_numeros = 0

while True:
    numero = int(input("digite um número ou pode optar por encerrar digitando 0. "))
    if numero == 0:
        break
    soma += numero
    quantidade_numeros += 1
if quantidade_numeros > 0:
    media = soma / quantidade_numeros
    print(f"\nquantidade de números digitados: {quantidade_numeros}")
    print(f"soma dos números: {soma}")
    print(f"média aritmética: {media}")

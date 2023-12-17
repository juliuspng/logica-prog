def notasd(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidadenotas = [0] * len(notas)  

    for i in range(len(notas)):
        quantidadenotas[i] = valor // notas[i]
        valor %= notas[i]

    return notas, quantidadenotas  


valor = int(input("Digite um valor inteiro:"))


notas, quantidadenotas = notasd(valor)


print(f"\nvalor lido: {valor}")
print("relação de notas:")
for i in range(len(quantidadenotas)):
    if quantidadenotas[i] > 0:
        print(f"{quantidadenotas[i]} nota(s) de {notas[i]}")
valor = int(input("Digite um valor inteiro: "))
c_100 = c_50 = c_20 = c_10 = c_5 = c_2 = c_1 = 0
while valor > 0:
    if valor >= 100:
        c_100 += 1
        valor -= 100
    elif valor >= 50:
        c_50 += 1
        valor -= 50
    elif valor >= 20:
        c_20 += 1
        valor -= 20
    elif valor >= 10:
        c_10 += 1
        valor -= 10
    elif valor >= 5:
        c_5 += 1
        valor -= 5
    elif valor >= 2:
        c_2 += 1
        valor -= 2
    else:
        c_1 += valor
        valor = 0
        print(f"\nValor lido: {valor}\n")
print("Notas:")
print(f"  - {c_100} nota(s) de R$ 100,00")
print(f"  - {c_50} nota(s) de R$ 50,00")
print(f"  - {c_20} nota(s) de R$ 20,00")
print(f"  - {c_10} nota(s) de R$ 10,00")
print(f"  - {c_5} nota(s) de R$ 5,00")
print(f"  - {c_2} nota(s) de R$ 2,00")
print(f"  - {c_1} nota(s) de R$ 1,00")
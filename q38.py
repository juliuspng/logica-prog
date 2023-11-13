idade_dias = int(input("Digite a idade em dias: "))
anos = idade_dias // 365
idade_dias %= 365
meses = idade_dias // 30
dias = idade_dias % 30
print(f"\nIdade: {anos} anos, {meses} meses e {dias} dias")
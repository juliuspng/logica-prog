numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))
numero3 = float(input("digite o terceiro número: "))

maior = menor = numero1

if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
print(f"maior={maior}")
print(f"menor={menor}")
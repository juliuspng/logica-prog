#a.
for numero in range(1, 101):
    print(numero)
#b.
for numero in range(50, 101, 2):
    print(numero)
#c.
for numero in range(10, -1, -1):
    print(numero)
print("BOOOMMMM")

#d.
limite = int(input("digite um valor: "))
escolha = input("você quer ver os números pares (digite 'par') ou ímpares (digite 'ímpar')? ")

if escolha == 'par':
    for numero in range(2, limite + 1, 2):
        print(numero)
elif escolha == 'ímpar':
    for numero in range(1, limite + 1, 2):
        print(numero)
else:
    print("opção inválida, digite 'par' ou 'ímpar'.")


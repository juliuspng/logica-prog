#a. essa eu não entendi

#b.
numero1 = int(input("digite o primeiro número: "))
numero2 = int(input("digite o segundo número: "))

quociente = 0
resto = numero1

while resto >= numero2:
    resto -= numero2
    quociente += 1

print(f"a divisão inteira de {numero1} por {numero2} é: {quociente}")
print(f"o resto da divisão de {numero1} por {numero2} é: {resto}")
#a.
import random
#b.
numero_secreto = random.randint(1, 100)
#c.
palpite = 0
#d.
while palpite != numero_secreto:
    
    palpite = int(input("Digite seu palpite (entre 1 e 100): "))

#e.
    if palpite > numero_secreto:
        print("Tente um número menor.")
    elif palpite < numero_secreto:
        print("Tente um número maior.")

#f.
print(f"Parabéns!! Você acertou o número secreto: {numero_secreto}")
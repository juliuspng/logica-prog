T = [-10, -8, 0, 1, 2, 5, -2, -4]

minima = float('inf')  
maxima = float('-inf')  
soma = 0

for temperatura in T:
    if temperatura < minima:
        minima = temperatura
    if temperatura > maxima:
        maxima = temperatura
    soma += temperatura

media = soma / len(T)

print(f"menor temperatura: {minima}°C")
print(f"maior temperatura: {maxima}°C")
print(f"temperatura média: {media:.2f}°C")




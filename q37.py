tempo_segundos = int(input("Digite o tempo de duração em segundos: "))
horas = tempo_segundos // 3600
tempo_segundos %= 3600
minutos = tempo_segundos // 60
segundos = tempo_segundos % 60
print(f"\nTempo de duração: {horas:02d}:{minutos:02d}:{segundos:02d}")
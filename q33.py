tempo_viagem = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Digite a velocidade média durante a viagem (em km/h): "))
distancia_percorrida = velocidade_media * tempo_viagem
eficiencia_automovel = 12
litros_necessarios = distancia_percorrida / eficiencia_automovel
print(f"\nPara a viagem de {tempo_viagem:.2f} horas, a uma velocidade média de {velocidade_media:.2f} km/h:")
print(f"Distância percorrida: {distancia_percorrida:.2f} km")
print(f"Quantidade de litros necessários: {litros_necessarios:.2f} litros")
distancia_total = float(input("Digite a distância total percorrida (em km): "))
combustivel_gasto = float(input("Digite o total de combustível gasto (em litros): "))
consumo_medio = distancia_total / combustivel_gasto
print(f"O consumo médio do automóvel é: {consumo_medio:.2f} km/l")
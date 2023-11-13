valor_monetario = float(input("Digite um valor monetário (duas casas decimais): "))
valor_centavos = int(valor_monetario * 100)
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
quantidade_notas = {}
quantidade_moedas = {}
for nota in notas:
    quantidade_notas[nota] = valor_centavos // (nota * 100)
    valor_centavos %= nota * 100
for moeda in moedas:
    quantidade_moedas[moeda] = valor_centavos // int(moeda * 100)
    valor_centavos %= int(moeda * 100)
    print("\nRelação de notas e moedas necessárias:")
for nota, quantidade in quantidade_notas.items():
    print(f"{quantidade} nota(s) de R$ {nota:.2f}")
for moeda, quantidade in quantidade_moedas.items():
    print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")
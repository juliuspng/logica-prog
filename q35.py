lado_quadrado = float(input("Digite o valor do lado do quadrado: "))
perimetro = 4 * lado_quadrado
area = lado_quadrado ** 2
diagonal = lado_quadrado * (2 ** 0.5)  # 2 elevado à 0.5 é a raiz quadrada de 2
print(f"\nPara um quadrado com lado {lado_quadrado}:\n")
print(f"Perímetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")
print(f"Diagonal: {diagonal:.2f}")
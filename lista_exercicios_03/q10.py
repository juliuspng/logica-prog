#a.
def calcular_area_quadrado(lado):
    return lado ** 2
lado_quadrado = 4
area_quadrado = calcular_area_quadrado(lado_quadrado)
print(f"A área do quadrado com lado {lado_quadrado} é {area_quadrado}.")

#b.
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2
base_triangulo = 5
altura_triangulo = 8
area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
print(f"A área do triângulo com base {base_triangulo} e altura {altura_triangulo} é {area_triangulo}.")

#c.

def calcular_area_quadrado(lado, exibir=False):
    area = lado ** 2
    if exibir:
        print(f"a área do quadrado com lado {lado} é {area}.")
    return area

def calcular_area_triangulo(base, altura, exibir=False):
    area = (base * altura) / 2
    if exibir:
        print(f"a área do triângulo com base {base} e altura {altura} é {area}.")
    return area

lado_quadrado = 4
area_quadrado = calcular_area_quadrado(lado_quadrado, exibir=True)

base_triangulo = 5
altura_triangulo = 8
area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo, exibir=True)
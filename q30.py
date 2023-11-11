a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

area_triangulo = (a * c) / 2
area_circulo = 3.14159 * c**2
area_trapezio = ((a + b) * c) / 2
area_quadrado = b**2
area_retangulo = a * b

print(f"\nÁrea do triângulo retângulo: {area_triangulo:.2f}")
print(f"Área do círculo: {area_circulo:.2f}")
print(f"Área do trapézio: {area_trapezio:.2f}")
print(f"Área do quadrado: {area_quadrado:.2f}")
print(f"Área do retângulo: {area_retangulo:.2f}")


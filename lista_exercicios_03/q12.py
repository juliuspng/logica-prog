#abordagem recursiva

def contagem_regressiva_recursiva(n):
    if n <= 0:
        print("contagem regressiva concluída!")
    else:
        print(n)
        contagem_regressiva_recursiva(n - 1)

numero_usuario = int(input("digite um número para a contagem regressiva: "))
contagem_regressiva_recursiva(numero_usuario)

#abordagem interativa(eu acho)
def contagem_regressiva_interativa(n):
    while n > 0:
        print(n)
        n -= 1
    print("contagem regressiva concluída!")

numero_usuario = int(input("digite um número para a contagem regressiva: "))
contagem_regressiva_interativa(numero_usuario)
def exibir_tabuada(operacao):
    print(f"\ntabuada de {operacao}:")
    for i in range(1, 11):
        resultado = 0
        if operacao == 'adição':
            resultado = numero + i
        elif operacao == 'subtração':
            resultado = numero - i
        elif operacao == 'multiplicação':
            resultado = numero * i
        elif operacao == 'divisão':
            resultado = numero / i
    print(f"{numero} {operacao} {i} = {resultado}")

while True:
    
    print("\nescolha uma opção:")
    print("1. adição")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. sair")

    escolha = input("digite o número da opção desejada: ")

    if escolha == '5':
        print("Fechou")
        
    if escolha in ['1', '2', '3', '4']:
        
        numero = float(input("digite um número para a operação: "))

        if escolha == '1':
            exibir_tabuada('adição')
        elif escolha == '2':
            exibir_tabuada('subtração')
        elif escolha == '3':
            exibir_tabuada('multiplicação')
        elif escolha == '4':
            exibir_tabuada('divisão')
    else:
        print("opção inválida. tente novamente.")






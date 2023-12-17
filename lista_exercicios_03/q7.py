def verifica_parenteses(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append('(')
        elif caractere == ')':
            if not pilha:
                return False  
            pilha.pop()

    return not pilha
expressao = input("digite uma expressão com parênteses: ")

if verifica_parenteses(expressao):
    print("os parênteses estão balanceados.")
else:
    print("os parênteses não estão balanceados.")


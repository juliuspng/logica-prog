#passagem por objeto
def alterar_lista(lista):
    lista.append(3) #vai adicionar elemento a lista
    print("Dentro da função:", lista)

minha_lista = [1, 2] #sendo essa a lista inicial

alterar_lista(minha_lista)
print("fora da função:", minha_lista) # resultado 

#passagem por valor
def incrementar_numero(numero):
    numero += 1
    print("dentro da função:", numero)

meu_numero = 4

incrementar_numero(meu_numero)
print("fora da função:", meu_numero)

#acredito que a melhor forma de diferenciar seja pelo uso das palavras: incrementar e adicionar onde um não vai alterar o valor original


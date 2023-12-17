def contem_item(lista, item):
    for elemento in lista:
        if elemento == item:
            return True
    return False

def lista_sem_repeticao(lista1, lista2):
    lista_resultante = []

    for item in lista1:
        if not contem_item(lista_resultante, item):
            lista_resultante.append(item)

    for item in lista2:
        if not contem_item(lista_resultante, item):
            lista_resultante.append(item)

    return lista_resultante


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

resultado = lista_sem_repeticao(lista1, lista2)

print("lista 1:", lista1)
print("lista 2:", lista2)
print("lista resultante (sem elementos repetidos):", resultado)
def ordenar_lista(lista):
    n = len(lista)

    for i in range(n - 1):

        indice_minimo = i

        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        tmp = lista[i]
        lista[i] = lista[indice_minimo]
        lista[indice_minimo] = tmp

minha_lista = [7, 4, 3, 12, 8]

ordenar_lista(minha_lista)

print("lista ordenada:", minha_lista)
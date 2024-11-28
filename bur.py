
def bubble(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# lista
listilla = [64, 34, 25, 12, 22, 11, 90]

# lista original
print("Lista original:", listilla)

# ordenar lista
lista_ordenada = bubble(listilla)

# mostrar lista ordenada
print("Lista ordenada:", lista_ordenada)

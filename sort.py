def quick_sort(lista):
    if len(lista) <= 1:  
        return lista
    
    pivote = lista[-1]  # el último elemento como pivote
    menores = [x for x in lista[:-1] if x <= pivote]  # elementos menores o iguales al pivote
    mayores = [x for x in lista[:-1] if x > pivote]   # elementos mayores al pivote
    
    return quick_sort(menores) + [pivote] + quick_sort(mayores)  # ordenar y combinar

# Lista
lista = [8, 3, 1, 7, 0, 10, 2]

# lista original
print("Lista original:", lista)

# ordenar la lista
lista_ordenada = quick_sort(lista)

# mostrar lista ordenada
print("Lista ordenada:", lista_ordenada)

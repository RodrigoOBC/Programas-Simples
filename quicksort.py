def quicksort(lista):
    if lista:
        left = [x for x in lista if x < lista[0]]
        right = [x for x in lista if x > lista[0]]
        if len(left) > 1:
            left = quicksort(left)
        if len(right) > 1:
            right = quicksort(right)
        return left + [lista[0]] * lista.count(lista[0]) + right
    return []

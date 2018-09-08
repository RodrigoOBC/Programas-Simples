def bubble_sort(vetor):
    tamanho = len(vetor) - 1
    trocou = False
    while not trocou:
        trocou = True
        for i in range(tamanho):
             if vetor[i] > vetor[i + 1]:
                 vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                 trocou = False
                 print(vetor)
    return vetor


print(bubble_sort([13,40,8,30,9,15,2]))
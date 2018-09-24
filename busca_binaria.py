def busca(vetor,buscado):
    meio = (len(vetor)-1)//2
    if meio < buscado:
        for i in range(meio,len(vetor)-1):
            if buscado == vetor[i]: return 'existe'

    if meio > buscado:
        for i in range(meio, 0):
            if buscado == vetor[i]: return 'existe'

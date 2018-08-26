def mostrar_caminhos(grafo, caminho, final):
    if caminho[-1] == final:
        yield caminho
        return
    for vizinho in G[caminho[-1]]:
        if vizinho in caminho:
            continue
        for caminho_maior in mostrar_caminhos(grafo, caminho + [vizinho], final):
            yield caminho_maior

G = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D'], 'D': ['B', 'C']}
for caminho in mostrar_caminhos(G, ['A'], 'D'):
    print (caminho)
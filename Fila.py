import heapq


class fila_prioridade:

    def __init__(self):
        self.fila = []
        self.indice = 0

    def inserir(self, item, prioridade):
        '''
            ou o famoso push
        '''
        heapq.heappush(self.fila, (-prioridade, self.indice, item))
        self.indice += 1

    def remover(self):
        '''
        o famoso pop
        '''
        return heapq.heappop(self.fila)[-1]


class Item:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

if __name__ == '__main__':
    fila = fila_prioridade()
    fila.inserir(Item('Marcos'),28)
    fila.inserir(Item('João'),30)
    fila.inserir(Item('Maria'),18)
    print(fila.remover())
    print(fila.remover())
    print(fila.remover())
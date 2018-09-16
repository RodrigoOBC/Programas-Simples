class PA:
    def __init__(self,pa):
        self.a1 = pa[0]
        self.ak = pa[-1]
        self.k = len(pa)
        self.r = (pa[0] - pa[1]) * -1

    def soma_PA(self):
        return ((self.a1 + self.ak) * self.k)//2

    def encontrar_termo_n(self,n):
        return  self.a1 + (n - 1) * self.r
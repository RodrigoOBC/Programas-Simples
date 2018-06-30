####
#
# Pensado e realizado pelo Rodrigo de Brito de Oliveira Cabral com a Ajuda do  Hallef Ramos
#
####
from abc import abstractmethod

@abstractmethod
class geometria():
    pi = 3, 14


    def perimetro(self):
        pass

    def area(self):
        pass

    def diagonal(self):
        pass



class Triangulo(geometria):

    def perimetro(self, lado):
        return lado * 3

    def area(self,b,h):
        return (b*h)/2

    def hipotenusa(self, b, h):
        return (b**2 + h**2)**0.5


class Quadrado(geometria):

    def perimetro(self, lado):
        return lado*4

    def area(self, lado):
        return lado*2

    def diagonal(self, lado):
        return self.area(lado)**0.5



class Retangulo(geometria):

    def perimetro(lado):
        return lado * 4

    def area(b, h):
        return b * h

    def diagonal(b, h):
        return (b ** 2 + h ** 2) ** 0.5

class Trapezio(geometria):
    def perimetro(self, lado, b, B):
        return B + b + (2*lado)

    def area(self, h, b, B):
        return ((B + b)*h)/2


class Circulo(geometria):

    def area(self, r):
        return self.pi * r**2

    def perimetro(self, r):
        return (self.pi*2)*r

    def diametro(self, r):
        return r*2

    def setor_circular(self,R,n):
        return ((self.pi*(R**2))/360)*n

    def coroa_circular(self,R,r):
        return self.pi*(R**2 - r**2)


class Losangolo(geometria):

    def area(self,D,d):
        return (0,5*D)*d

    def perimetro(self,lado):
        return lado*4


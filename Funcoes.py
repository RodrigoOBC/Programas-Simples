####
#
# Pensado e realizado pelo Rodrigo de Brito de Oliveira Cabral com a Ajuda do  Hallef Ramos
#
####
from abc import abstractmethod

@abstractmethod
class geometria():

    def __init__(self):
        self.pi = 3.14


    def perimetro(self):
        pass

    def area(self):
        pass

    def diagonal(self):
        pass


@abstractmethod
class Algebra():

    def __init__(self):
        pass


class Triangulo(geometria):

    def perimetro(self, lado):
        return lado * 3

    def area(self, b, h):
        return (b*h)/2

    def hipotenusa(self, b, h):
        return (b**2 + h**2)**0.5


class Quadrado(geometria):

    def perimetro(self, lado):
        return lado*4

    def area(self, lado):
        return lado*2

    def diagonal(self, lado):
        return round(lado*(2**0.5),2)


class Retangulo(geometria):

    def perimetro(self,lado):
        return lado * 4

    def area(self,b, h):
        return b * h

    def diagonal(self,b, h):
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


class Polinomios(Algebra):

    def distributiva(self,a,b):
        return a**2+a*b*2+b

class Sequencias(Algebra):

    def soma_PA(self,a1,ak,k):

        '''
        :param a1: primeiro Termo da PA
        :param ak: ULTIMO Termo da PA
        :param k: TOTAL DE TERMOS DA PA
        :return:
        '''

        return ((a1+ak)*k)/2

    def Encontrar_termo_n(self, a1, K, r):

        '''
        :param a1: primeiro Termo da PA
        :param K: posiçao a ser encontrada
        :param r: rasao da pa
        :return:
        '''

        return a1+(K-1)*r
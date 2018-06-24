####
#
# Pensado e realizado pelo Rodrigo de Brito de Oliveira Cabral com a Ajuda da amiga nathy
#
####

class Triangulo:

    def perimetro(self, lado):
        return lado * 3

    def area(self,b,h):
        return (b*h)/2

    def hipotenusa(self, b, h):
        return (b**2 + h**2)**0.5


class Quadrado:

    def perimetro(self, lado):
        return lado*4

    def area(self, lado):
        return lado*2

    def diagonal(self, lado):
        return self.area(lado)**0.5



class Retangulo:

    def perimetro(self, lado):
        return lado * 4

    def area(self, b, h):
        return b * h
    
    def diagonal(self, b, h):
        return (b**2 + h**2)**0.5

class Trapezio:
    def perimetro(self, lado, b, B):
        return B + b + (2*lado)

    def area(self, h, b, B):
        return ((B + b)*h)/2


class Circulo:
    pi = 3,14

    def area(self, r):
        return self.pi * r**2

    def perimetro(self, r):
        return (self.pi*2)*r

    def diametro(self, r):
        return r*2

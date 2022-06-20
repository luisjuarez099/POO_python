from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def perimetro(self):
        pass
    def area(self):
        pass

class Cuadrado(Forma):
    def __init__(self,lados) -> None:
        self.lados=lados
    def perimetro(self):
        return self.lados * 4
    def area(self):
        return self.lados ** 2
class Triangulo(Forma):
    def __init__(self,base=float,altura=float,lado=float) -> None:
        self.altura=altura
        self.base=base
        self.lado=lado
    def perimetro(self):
        return self.lado * 3
    def area(self):
        return self.altura * self.base / 2
    
cuadrado=Cuadrado(5)
triangulo=Triangulo(12,15,5)

print(f"El perimetro de  {cuadrado.lados}  es de : {cuadrado.perimetro()}")
print(f"El Area de {cuadrado.lados}  es de : {cuadrado.area()}")

print(f"El perimetro de  {triangulo.lado}  es de : {triangulo.perimetro()}")
print(f"El Area del triangulo es base: {triangulo.base} X {triangulo.altura} es de : {triangulo.area()}")
        
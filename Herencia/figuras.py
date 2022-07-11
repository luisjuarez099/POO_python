
class Triangulo:
    def __init__(self,base,altura) -> None:
        self.base=base
        self.altura=altura
       
    def area(self):
        result=(self.base * self.altura)/2
        return result

class Rectangulo(Triangulo):
    def __init__(self, base, altura) -> None:
        super().__init__(base, altura)

    def perimetro(self):
        return 2*(self.base+self.altura)

if __name__=='__main__':
    triangulo=Triangulo(base=2,altura=4)
    print(triangulo.area())

    cuadrado=Rectangulo(4,6)
    print(cuadrado.perimetro())
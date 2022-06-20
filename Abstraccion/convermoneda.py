from abc import ABC,abstractmethod

class Moneda(ABC):
    @abstractmethod
    def EuaMx(self):#dollar eua -> peso mx
        pass
    @abstractmethod
    def CanMx(self):#dollar can -> peso mx
        print("Moneda Canadiense")

class AmeMx(Moneda):
    def __init__(self,cantidad,pesoMx=20.3638,pesocan=15.6333) -> None:
        self.pesoMx=pesoMx
        self.pesocan=pesocan
        self.cantidad=cantidad

    def EuaMx(self):
        return self.cantidad * self.pesoMx
    def CanMx(self):
        return self.cantidad * self.pesocan


#Instancias
Moneda1=AmeMx(100)
print(f"{Moneda1.cantidad} dolares Americanos a peso Mexicano es de {Moneda1.EuaMx()}")
print(f"{Moneda1.cantidad} dolares Canadiense a peso Mexicano es de {Moneda1.CanMx()}")


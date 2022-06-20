from abc import ABC,abstractmethod

class Moneda(ABC):
    @abstractmethod
    def EuaMx(self):#dollar eua -> peso mx
        pass
    @abstractmethod

    def CanMx(self):#dollar can -> peso mx
        pass

class MxEua(ABC):
    @abstractmethod
    def MxEua(self):
        pass

class AmeMx(Moneda):
    def __init__(self,cantidad,pesoeua=20.3638,pesocan=15.6333) -> None:
        self.pesoMx=pesoeua
        self.pesocan=pesocan
        self.cantidad=cantidad

    def EuaMx(self):
        return self.cantidad * self.pesoMx
    def CanMx(self):
        return self.cantidad * self.pesocan

class PesoMxaEua(MxEua):
    def __init__(self,monedaeua=int,pesoMx=0.0491681) -> None:
        self.pesoMx=pesoMx
        self.monedaeua=monedaeua
    def MxEua(self):
        return self.pesoMx * self.monedaeua

#Instancias
Moneda1=AmeMx(100)
print(f"{Moneda1.cantidad} dolares Americanos a peso Mexicano es de {Moneda1.EuaMx()}")
print(f"{Moneda1.cantidad} dolares Canadiense a peso Mexicano es de {Moneda1.CanMx()}")

mxeua=PesoMxaEua(2000)
print(f"{mxeua.monedaeua} Peso Mexicanos son {round(mxeua.MxEua(),2)} Dolares Americanos")

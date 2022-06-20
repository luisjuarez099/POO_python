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
    def MxEua(self):# mx -> dollar eua
        pass
    @abstractmethod
    def MxCan(self):# mx -> dollar can
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
    def __init__(self,moneda=int,pesoMx=0.0491681,pesoMxc=0.0640086) -> None:
        self.pesoMx=pesoMx
        self.pesoMxc=pesoMxc
        self.moneda=moneda
    def MxEua(self):
        return self.pesoMx * self.moneda
    def MxCan(self):
        return self.pesoMxc * self.moneda
#Instancias
Moneda1=AmeMx(100)
print(f"{Moneda1.cantidad} dolares Americanos a peso Mexicano es de {Moneda1.EuaMx()}")
print(f"{Moneda1.cantidad} dolares Canadiense a peso Mexicano es de {Moneda1.CanMx()}")

mxeua=PesoMxaEua(100)
print(f"{mxeua.moneda} Peso Mexicanos son {round(mxeua.MxEua(),2)} Dolares Americanos")
print(f"{mxeua.moneda} Peso Mexicanos son {round(mxeua.MxCan(),2)} Dolares Canadienses")

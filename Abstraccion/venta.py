from abc import ABC, abstractmethod
class Venta(ABC):
   
    @abstractmethod
    def descuento(self):
        pass

class Pago(Venta):
    def __init__(self,producto=str,precio=float,cantidad=int, descuento=float) -> None:
        self.producto=producto
        self.precio=precio
        self.cantidad=cantidad
        self.descuento=descuento

    def descuento(self):
        pago=self.precio * self.descuento
        return pago

pago1=Pago("Adidas",1200,10,10)
print(pago1.descuento())
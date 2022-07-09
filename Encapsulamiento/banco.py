

class Cuenta():
    def __init__(self,nombre,saldo,moneda) -> None:
        self.nombre=nombre
        self.__saldo=saldo
        self.moneda=moneda

    @property
    def saldo(self):
        self.__saldo

    @saldo.setter
    def saldo(self,saldoN):
        self.__saldo= saldoN

    @saldo.deleter
    def saldo(self):
        print(f"Cuenta pasada {self._Cuenta__saldo}, Dinero Ingresado  {cliente.saldoN}")
        print(f"Total de salado en cuenta: {self._Cuenta__saldo + cliente.saldoN}")
        del self.__saldo


cliente=Cuenta("Luis",1200,"MXN")
print(f"Sus Datos de cuenta: {cliente.nombre} ,{cliente._Cuenta__saldo} ,{cliente.moneda}")

cliente.saldoN=int(input("Ingresa tu Dinero: "))
print(f"Su saldo es de {cliente.saldoN}")
del cliente.saldo
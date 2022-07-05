from abc import ABC,abstractclassmethod

'''Implementamos nuestra clase Abtracta'''

class Transporte(ABC):
    __Compania=None
    __Marca=None
    __Llantas=0
    __Color=None
    __Velocidad=None
    __CapCarga=None

    @abstractclassmethod
    def Llantas():
        pass

    @abstractclassmethod
    def Empresa():
        pass

    @abstractclassmethod
    def Color():
        pass

    @abstractclassmethod
    def Velocidad():
        pass

    @abstractclassmethod
    def CapCarga(): #Capacidad de carga
        pass

class Carro(Transporte):
    Transporte.__Compania="MAZDA"
    Transporte.__Marca="MAZDA 2 HATCHBACK i SPORT"
    Transporte.__Llantas=4
    Transporte.__Color="Rojo"
    Transporte.__Velocidad=109
    Transporte.__CapCarga=1501
    def Llantas(self):
        print(f"{Transporte.__Llantas} Llantas")
    def Color():
        print(f"Color: {Transporte.__Color}")
    def Empresa(self):
        print(f"Mi Carro {Transporte.__Marca} de la Compania {Transporte.__Compania}")
    def Velocidad(self):
        print(f"Su velocidad es de HP (Hourse Potencial) {Transporte.__Velocidad} rpm")
    def CapCarga(self):
        print(f"Su capacidad de carga es de TM (Toneladas Mercancia): {Transporte.__CapCarga}")

class Motocicleta(Transporte):
    Transporte.__Compania="Italika"
    Transporte.__Marca="RT200"
    Transporte.__Llantas=2
    Transporte.__Color="Negra"
    Transporte.__Velocidad=116
    Transporte.__CapCarga=150

    def Llantas(self):
        print(f"{Transporte.__Llantas} Llantas")
    def Color():
        print(f"Color: {Transporte.__Color}")
    def Empresa(self):
        print(f"Mi Motocicleta {Transporte.__Marca} de la Compania {Transporte.__Compania}")
    def Velocidad(self):
        print(f"Su velocidad es de: {Transporte.__Velocidad} Km/h ")
    def CapCarga(self):
        print(f"Su capacidad de carga es de: {Transporte.__CapCarga} Kg")


carro=Carro()#Instanciamos
carro.Empresa()
carro.Llantas()
carro.Velocidad()
carro.CapCarga()

print()#Separacion de las dos intancias

moto=Motocicleta()#Instanciamos
moto.Empresa()
moto.Llantas()
moto.Velocidad()
moto.CapCarga()

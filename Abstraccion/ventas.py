'''
Pagos de Registro:

-Ingreso= Variables de trabajadores. 
-ISR= Consultar tabla de ISR 2022.

Vendedor, Ope.Autobuses, Dueno de Negocio.
'''
from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    __Nombre=None
    __Puesto=None
    __ingreso=None
    __lim_inferior=None

    @abstractclassmethod
    def Nombre():
        pass
    @abstractclassmethod
    def Puesto():
        pass
    @abstractclassmethod
    def Ingreso():
        pass
    @abstractclassmethod
    def Isr():
        pass
    @abstractclassmethod
    def Pago_Isr():
        pass
    
class Vendedor(Trabajador):
    Trabajador.__Nombre="Guadalupe Fonseca Ortiz"
    Trabajador.__Puesto="Vendedora"
    Trabajador.__ingreso=8000
    Trabajador.__lim_inferior=5470.92

    def Nombre(self):
        print(f"Nombre: {Trabajador.__Nombre}")

    def Puesto(self):
        print(f"Puesto: {Trabajador.__Puesto}")

    def Ingreso(self):
        self.base= Trabajador.__ingreso - Trabajador.__lim_inferior
        print(f"Su ingreso es de:  {Trabajador.__ingreso}, menos ya incluido el limite inferior {Trabajador.__lim_inferior} de Ingreso")

        print(f"Total: {round(self.base,2)}")

    def Isr(self):
        #res=base - tasa = 10.88%
        self.res=self.base - 10.88
        print(f"Resultado {self.res}")
        #impuesto a retener= res - cuota fija
        self.imp_retener= self.res + 321.26 #<-- Cuota fija
        print(f"Impuesto a retener: {round(self.imp_retener,2)}")

    def Pago_Isr(self):
        print(f"Ingreso {Trabajador.__ingreso}, ISR a retener {round(self.imp_retener,2)} y Percepcion efectiva {round(Trabajador.__ingreso - self.imp_retener,2)}")

class Dueno(Trabajador):
    Trabajador.__Nombre="Mario Felipe Gallardo"
    Trabajador.__Puesto="Dueño"
    Trabajador.__ingreso=500000
    Trabajador.__lim_inferior=324845.01
    def Nombre(self):
        print(f"Nombre: {Trabajador.__Nombre}")

    def Puesto(self):
        print(f"Puesto: {Trabajador.__Puesto}")

    def Ingreso(self):
        #base= ingreso - limite inferior de ingreso
        self.base= Trabajador.__ingreso - Trabajador.__lim_inferior
        print(f"Su ingreso es de: {Trabajador.__ingreso} menos ya incluido el limite inferior (5470.92) de Ingreso")

        print(f"Total: {round(self.base,2)}")

    def Isr(self):
        #res=base - tasa = 10.88%
        self.res=self.base - 35.00
        print(f"Resultado {self.res}")
        #impuesto a retener= res - cuota fija
        self.imp_retener= self.res + 101876.90 #<-- Cuota fija
        print(f"Impuesto a retener: {round(self.imp_retener,2)}")

    def Pago_Isr(self):
        print(f"Ingreso {Trabajador.__ingreso}, ISR a retener {round(self.imp_retener,2)} y Percepcion efectiva {round(Trabajador.__ingreso - self.imp_retener,2)}")




vendedor=Vendedor()
vendedor.Nombre()
vendedor.Puesto()
vendedor.Ingreso()
vendedor.Isr()
vendedor.Pago_Isr()

print()

dueno=Dueno()
dueno.Nombre()
dueno.Puesto()
dueno.Ingreso()
dueno.Isr()
dueno.Pago_Isr()
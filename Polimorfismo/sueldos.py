class Empleado:
    def __init__(self,nombre,sueldomensual) -> None:
        self.nombre=nombre
        self.sueldomensual=sueldomensual

    def sueldoanual(self):
        sueldo=self.sueldomensual * 12*(1 + 1/100)
        print(f"Sueldo anual de {self.nombre} es de {sueldo} MXN")
class Contable(Empleado):
    def __init__(self, nombre, sueldomensual) -> None:
        super().__init__(nombre, sueldomensual)
    #polimorfismo
    def sueldoanual(self):
        sueldo=12 * self.sueldomensual*(1+4/100)
        print(f"Sueldo anual de {self.nombre} es de {sueldo} MXN")
class Vendedor(Empleado):
    def __init__(self, nombre, sueldomensual) -> None:
        super().__init__(nombre, sueldomensual)

    def sueldoanual(self):
        sueldo=12 * self.sueldomensual*(1+3/100)
        print(f"Sueldo anual de {self.nombre} es de {sueldo} MXN")

class Becario(Empleado):
    def __init__(self, nombre, sueldomensual) -> None:
        super().__init__(nombre, sueldomensual)

    def sueldoanual(self):
        sueldo=12 * self.sueldomensual
        print(f"Sueldo anual del becario {self.nombre} es de {sueldo} MXN")

empleado=Empleado("Juan",80)
contador=Contable("Emilio",60)
vendedor=Vendedor("Alejandra",120)
becario=Becario("Luis",65)

DATA=[empleado,contador,vendedor,becario]

for emp in DATA:
    emp.sueldoanual()

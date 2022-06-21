'''4.- carro a rentar (carro)
    -Economic
    -Sub
    -luxury
'''

class Economico:
    def __init__(self,marca,modelo,asientos,velMax,precioEco) -> None:
        self.marca=marca
        self.modelo=modelo
        self.asientos=asientos
        self.velMax=velMax
        self.precioEco=precioEco

    def Almacen_Econ(self):
        print(f"Marca {self.marca}, Modelo {self.modelo}, Asientos: {self.asientos}, VelMax: {self.velMax} Km/h, Precio de renta por dia: {self.precioEco} Pesos Mx")

class Sub(Economico):
    def __init__(self, marca, modelo, asientos, velMax,precioSub) -> None:
        super().__init__(marca, modelo, asientos, velMax,precioSub)
        self.precioSub=precioSub

    def Almacen_Sub(self):
        print(f"Marca {self.marca}, Modelo {self.modelo}, Asientos: {self.asientos}, VelMax: {self.velMax} Km/h, Precio de renta por dia: {self.precioSub} Pesos Mx")

class Luxury(Economico):
    def __init__(self, marca, modelo, asientos, velMax,precioLux) -> None:
        super().__init__(marca, modelo, asientos, velMax,precioLux)
        self.precioLux=precioLux
    def Almacen_Lux(self):
        print(f"Marca {self.marca}, Modelo {self.modelo}, Asientos: {self.asientos}, VelMax: {self.velMax} Km/h, Precio de renta por dia: {self.precioLux} Pesos Mx")

#Sub
carsub1=Sub("Nissan","X-Trail",4,220,350)
carsub2=Sub("Jeep","GZ=9000",2,180,410)
#Economico
careco1=Economico("Mazda","G-990",4,150,189)
careco2=Economico("Nissan","Centra",4,170,145)

#Luxury
carlux1=Luxury("Mercedez","AMG",2,350,590)
carlux2=Luxury("Tesla","X",4,390,600)

if __name__=="__main__":
    print("Sub")
    carsub1.Almacen_Sub()
    carsub2.Almacen_Sub()
    print()
    print("Economico")
    careco1.Almacen_Econ()
    careco2.Almacen_Econ()
    print()
    print("Luxur")
    carlux1.Almacen_Lux()
    carlux2.Almacen_Lux()


    


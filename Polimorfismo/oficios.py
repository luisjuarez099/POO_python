class Carpintero:
    def __init__(self,nombre,edad,ocupacion) -> None:
        self.nombre=nombre
        self.edad=edad
        self.ocupacion=ocupacion

    def ocupacion(self):
        print("Soy un carpintero que hago sillas. ")

class Policia(Carpintero):
    def __init__(self, nombre, edad, ocupacion) -> None:
        super().__init__(nombre, edad, ocupacion)

        def ocupacion(self):
            print("Yo cuido de la personas.")

class IngeCivil(Carpintero):
    def __init__(self, nombre, edad, ocupacion) -> None:
        super().__init__(nombre, edad, ocupacion)

        def ocupacion(self):
            print("Yo construllo puentes, edificios y Departamentos")

#Instanciar
if __name__=='__main__':
    
    carp=Carpintero("Eduerdo",45,"Carpintero")
    print(f"Mi nombre es {carp.nombre}, mi edad es {carp.edad} años y mi ocupacion es {carp.ocupacion}")

    inge=IngeCivil("Pedro",34,"Inge. Civil")
    print(f"Mi nombre es {inge.nombre}, mi edad es {inge.edad} años y mi ocupacion es {inge.ocupacion}")

    poli=Policia("Manuel",55,"Policia")
    print(f"Mi nombre es {poli.nombre}, mi edad es {poli.edad} años y mi ocupacion es {poli.ocupacion}")

    
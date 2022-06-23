'''Utilizaremos el __str__ de la clase 
en la captura de datos de estudiantes para 
tarjeta del transporte publico'''

class Informacion:
    emision="10/08/2022"
    vigencia="10/08/2023"

    def __init__(self,nombre,edad,escuela,grado) -> None:
        self.nombre=nombre
        self.edad=edad
        self.escuela=escuela
        self.grado=grado

    def __str__(self):
        alumno=f"Nombre: {self.nombre}, Edad: {self.edad}, Escuela: {self.escuela}, Grado: {self.grado}"
        return alumno

    def __eq__(self,other) -> bool:
        if isinstance(other,Informacion):
            if self.nombre == other.nombre:
                return True 
            else:
                return False 
    
    def __repr__(self) -> str:
        return f" Nombre: {self.nombre}, Escuela: {self.escuela}, Edad: {self.edad} anios"

    def __hash__(self) -> int:
        return hash(self.edad)

    def __bool__(self):
        if self.edad>=18:
            print("Mayor de edad")
            return True
        print("Menor de edad")
        return False



alum=Informacion("Luis", 23, "UNEDL", "Universidad")
alum2=Informacion("Ernesto", 25, "UVM", "Preparatoria")
alum3=Informacion("Emilia", 35, "ITESO", "Universidad")


if __name__=="__main__":
    
    print(f"Fecha de emision: {Informacion.emision}")
    print(f"Fecha de vigencia: {Informacion.vigencia}")
    print(alum)
    print(alum2)
    print("Uso de __eq__")
    print(alum2==alum3)

    print("Uso de __repr__")
    print(repr(alum))
    print(repr(alum3))

    print("Uso de __hash__")
    print(hash(alum2))

    print("Uso de __bool__")
    print(bool(alum))

'''
SPECIAL METHODS
    __str__ 
    __repr__ # Devuelve la representación de cadena de un objeto
    __eq__ #Compara dos instancias  de clase
    __hash__
    __bool__
__del__

'''
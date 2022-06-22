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


alum=Informacion("Luis", 23, "UNEDL", "Universidad")
alum2=Informacion("Ernesto", 25, "UVM", "Preparatoria")

print(f"Fecha de emision: {Informacion.emision}")
print(f"Fecha de vigencia: {Informacion.vigencia}")
print(alum)
print(alum2)

'''
SPECIAL METHODS
    __str__ 
__repr__
__eq__
__hash__
__bool__
__del__

'''
from abc import ABC, abstractclassmethod

'''Calcularemos el salario de empleados de tiempo completo, medio tiempo y estudiante.
como tambien veremos si gana mucho o poco. '''

class Empleado(ABC):
    def __init__(self,nombre,edad,puesto) -> None:
        self.nombre=nombre
        self.edad=edad
        self.puesto=puesto


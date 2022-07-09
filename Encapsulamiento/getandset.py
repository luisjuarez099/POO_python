#Vida Personal de roberto

#Protegido
# class Persona():
#     def __init__(self,nombre,ocupacion,edad) -> None:
#         self.nombre=nombre#publico
#         self._ocupacion=ocupacion#protegido
#         self._edad=edad#protegido
    
#Privados
class Mascota():
    def __init__(self,nombre,animal) -> None:
        self.__nombre=nombre
        self.__animal=animal

#----getter
    @property #getter
    def animal(self):
        return self.__animal 
    @property #Funciona como un getter 
    def nombre(self):
        return self.__nombre

#----setter

    @animal.setter #setter
    def animal(self,nuevoanimal):
        self.__animal=nuevoanimal
    @nombre.setter
    def nombre(self,nuevonombre):
        self.__nombre=nuevonombre    


#----del
    @nombre.deleter
    def nombre(self):
        print(f"Cambiamos nombre del animal a {mascota.nombre}")
        del self.__nombre

# alumno=Persona("Roberto","Estudiar",23)
# print(f"Mi nombre es {alumno.nombre}, mi ocupacion es {alumno._ocupacion} y tengo {alumno._edad} años de edad")
      
mascota=Mascota("Queso","Gato")
print(f"{mascota.nombre} es el nombre del {mascota.animal}")

mascota.nombre="Cokita"
print(f"{mascota.nombre} es el nombre del {mascota.animal}")
del mascota.nombre

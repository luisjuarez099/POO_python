
class Alumno():
    def __init__(self,nombre,apellido) -> None:
        self.nombre=nombre 
        self.apellido=apellido
    
    @property
    def nomalum(self):
        return self.nombre + ' '+ self.apellido

    @nomalum.setter
    def nomalum(self,nombrecompleto):
        self.nombre,self.apellido=nombrecompleto.split(' ')

alumno1=Alumno("Juan","Rodriguez")
print(f"Hola {alumno1.nombre} {alumno1.apellido} ")


alumno1.nomalum="Luis Juarez"
print(alumno1.nomalum)
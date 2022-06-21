class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre=nombre
        self.edad=edad
        
    def Presentarse(self):
        print(f"Hola, me llamo {self.nombre}, mi edad es de {self.edad} anios y en la universidad {self.escuela}  estudio la carrera de {self.carrera} con un promedio de {self.promedio}. Mucho gusto")


# persona=Persona("emilio",23,"UNEDL",80)
# persona.Presentarse()

class Alumno(Persona):#Hereda de la clase Persona
    #propio constructor
    def __init__(self, nombre, edad, escuela,promedio,carrera) -> None:
        super().__init__(nombre, edad)#de la clase super clase
        self.promedio=promedio
        self.carrera=carrera
        self.escuela=escuela

    def SigSemestre(self):
        if self.promedio >= 70 and self.promedio <=100:
            print("Pasas al siguiente semestre")
        else:
            print("Estas reprobado.")

class Trabajador(Persona):
    def __init__(self, nombre,edad, sueldo, puesto) -> None:
        super().__init__(nombre, edad)
        self.sueldo=sueldo
        self.puesto=puesto
    def calcularSueldo(self):
        return  self.sueldo / 6

alumno1=Alumno("Luis",23,"UNEDL",65,"Ing. Software")
alumno1.Presentarse()
alumno1.SigSemestre()

trabajador=Trabajador("Julio",55,1200,"programador")
print(f"Hola, me llamo {trabajador.nombre}, mi edad es de {trabajador.edad} anios y trabajo como {trabajador.puesto} Mucho gusto")
print(f"Ganas por dia : {trabajador.calcularSueldo()} pesos")
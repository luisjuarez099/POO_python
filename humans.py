from ast import Constant


class Humans():
    def __init__(self,name:str,age:int,occupation:str,sex:str,stature:float) -> None:
        #Manejo de exepciones
        assert age>=0, f"La edad no puede ser menor que cero"
        #Se inicializa el objeto de la clase Humans
        self.name=name
        self.age=age
        self.occupation=occupation
        self.sex=sex
        self.stature=stature
    def pies_to_meters(self):
        return self.stature/3.28
        

#Instanciar
#Person=Humans():
Person1=Humans("Arturo",20,"Policia","Hombre",5.8)
Person2=Humans("Zara",23,"Estudiante","Muejer",5.3)

#Person 1
print(f"Su nombre es {Person1.name}")
print(f"Su edad es {Person1.age} años")
print(f"Su ocupacion es: {Person1.occupation}")
print(f"Su Sexo es: {Person1.sex}")
print("La estatura de", Person1.name ," es de ", round(Person1.pies_to_meters(),2),"metros")

print()#Espacio

#Persona 2
print(f"Su nombre es {Person2.name}")
print(f"Su edad es {Person2.age} años")
print(f"Su ocupacion es: {Person2.occupation}")
print(f"Su Sexo es: {Person2.sex}")
print("La estatura de", Person2.name ," es de ", round(Person2.pies_to_meters(),2),"metros")








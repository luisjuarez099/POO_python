class Circulo:
    def __init__(self,radio) -> None:
        self.__radio=radio
        self.__pi=3.1416
    def perimetro(self):
        return 2*self.__pi * self.__radio
    def area(self):
        return self.__pi * self.__radio**2
    #Hacemos privado pi
    def getPi(self):
        return self.__pi #privado
    
    def setRadio(self,valor):
        if type(valor)==int or type(valor)==float:
            if valor>0:
                self.__radio=valor
                print(f"El radio se ha modificado: {self.__radio}")
            else:
                print("El radio no puede ser negativo")
        else:
            print("El radio tiene que ser un numero")


circulo=Circulo(2.5)

print(circulo.perimetro())
print(circulo.area())
print(f"La constante pi es {circulo.getPi()} ")#getPi()
circulo.setRadio(34)
circulo.setRadio(-34)
circulo.setRadio("Hola")









'''
_atributo=protegido
__atributo=privado

cuando utilizamos el metodo PRIVADO que es:
__atributo, la manera correcta de imprimir seria:

****
print(f"La constante pi es {circulo._Circulo__pi} ")
****
_Clase__Atributo/Metodo, de esta manera imprime para que no salga el error: AttributeError: 'Circulo' object has no attribute '__pi'

Cuando utilizamos el metodo PROTEGIDO que es:
_atributo podremos seguir imprimiendo de la  manera:

****
print(f"La constante pi es {circulo._pi} ")
****

'''
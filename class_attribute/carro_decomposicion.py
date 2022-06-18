class Auto:

    def __init__(self,modelo,marca,color) -> None:
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self._estadi0="reposo" #variable privada se inica usando:  _<variable>
        self._motor=Motor(cilindro=4)
    def acelerar(self,tipo='despacio'):
        if tipo =='rapido':
            self._motor.gasolina(10)
        else:
            self._motor.gasolina(3)

class Motor:

    def __init__(self,cilindro,tipo="gasolina") -> None:
        self.cilindro=cilindro
        self.tipo=tipo
        self._temperatura=0

    def gasolina(self,cantidad):
        pass

class Llantas:
    def __init__(self,ancho=int,alto=int,diametro=int) -> None:
        self.ancho=ancho
        self.alto=alto
        self.diametro=diametro
invierno=Llantas(10,50,30)
print(invierno.ancho())



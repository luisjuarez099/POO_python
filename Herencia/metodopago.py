class Tcredito():
    def __init__(self,nombre,banco,vigencia,limite_credito) -> None:
        self.nombre=nombre#Nombre de la persona
        self.banco=banco#Banco asociado
        self.vigencia=vigencia#cuado vence la tarjeta
        self.limite_credito=limite_credito #saldo disponible
    def SinIntereses(self):
        print("6 Meses de pagos sin intereses")
        
    def PagoRenta(self):
        pass
    
class Tdebito(Tcredito):
    def __init__(self, nombre, banco, vigencia, saldo) -> None:
        super().__init__(nombre, banco, vigencia, saldo)
        self.saldo=saldo

    def PagoRenta(self):
        pass
    


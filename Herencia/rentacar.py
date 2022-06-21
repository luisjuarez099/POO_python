
class Cliente:
    def __init__(self,nombre,ID,correo) -> None:
        self.nombre=nombre
        self.ID=ID
        self.correo=correo        
    def datos(self):
        print(f"Nombre del cliente: {self.nombre}, ID del Cliente : {self.ID},Correo electronico: {self.correo} ")


class Vendedor(Cliente):
    def __init__(self, nombre, IDV,correo) -> None:
        super().__init__(nombre, IDV,correo)
        self.IDV=IDV
    def atiende(self):
        print(f"Vendedor: {self.nombre}, ID del Vendedor: {self.IDV},Correo electronico: {self.correo} ")

cliente1=Cliente("Luis","CLJP9055","jardinesymas@gmial.com")
vendedor=Vendedor("Emilio","VEK5571","EmilioVEK5571@rentacar.com")



if __name__=="__main__":
    cliente1.datos()
    vendedor.atiende()


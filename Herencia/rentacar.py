
class Cliente:
    def __init__(self,nombre,ID) -> None:
        self.nombre=nombre
        self.ID=ID
    def saludo(self):
        print(f"Nombre del cliente: {self.nombre}, ID del Cliente : {self.ID}")


class Vendedor(Cliente):
    def __init__(self, nombre, IDV) -> None:
        super().__init__(nombre, IDV)
        self.IDV=IDV
    def atiende(self):
        print(f"Vendedor: {self.nombre}, ID del Vendedor: {self.IDV}")

cliente=Cliente("Luis","@CLJP9055")
vendedor=Vendedor("Emilio","$VEK5571")



if __name__=="__main__":
    cliente.saludo()
    vendedor.atiende()


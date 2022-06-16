'''Se va a crear el proyecto de venta de telefonos usando el 
paradigma orientado a objetos
'''
class Item:
    #---------------------------Atributos de clase
    impuesto=0.16
    #---------------------------Atributos o caracteristicas
    def __init__(self,precio:float,modelo:str,marca:str):
        #Atributos de Inatancia
        self.modelo=modelo
        self.marca=marca
        self.precio=precio
    #-----------------------------Metodos. ACCIONES para calcular. 
    def Pago_total(self):
        #Pago total a pagar precio por cantidad. (Precio en Dollar)
        self.cantidad=int(input(f"Digta cantidad de Telefonos {telefono1.marca} que quiere: "))
        self.total=self.precio*self.cantidad
        return self.total

    def impuestos(self):
        #Estes es mi total de Impuesto a pagar.
        self.impuesto=self.total * Item.impuesto 
        self.precio_mas_impuesto=self.impuesto + self.total 
        return self.precio_mas_impuesto
    def envio_internacional(self,envio):
        '''***TERMINAR MI ENVIO CON PARAMETRO DENTRO DE ESTA FUNCIOS
        AVERIGUAR QUE ES CADA COSA ESCRITA DENTRO DE ESTE PROGRAMA'''
        pass
    
telefono1=Item(100,"AXP123","Xiomi")
print(f"Modelo es {telefono1.modelo}")
print(f"Marca del telefono: {telefono1.marca}")
print(f"Pago total del telefono: {telefono1.Pago_total()}")
print(f"Pago de Impuestos del producto: {telefono1.impuestos()} pesos")

print()

telefono2=Item(500,"13","Apple")
print(f"Modelo es {telefono2.modelo}")
print(f"Marca del telefono: {telefono2.marca}")
print(f"Pago total del telefono: {telefono2.Pago_total()}")
print(f"Pago de Impuestos del producto: {telefono2.impuestos()} pesos")


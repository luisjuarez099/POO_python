'''Se va a crear el proyecto de venta de telefonos usando el 
paradigma orientado a objetos
'''
class Item:
    #---------------------------Atributos de clase
    impuesto=0.16
    envio=30
    #---------------------------Atributos o caracteristicas de Instancia
    def __init__(self,precio:float,modelo:str,marca:str):#__init__: el constructor
        #Atributos de Inatancia. Inicializando variables de Instancia que apunta a memoria. 
        self.modelo=modelo
        self.marca=marca
        self.precio=precio
    #-----------------------------Metodos. ACCIONES para calcular. Metodos de Instancia.
    def Pago_total(self):
        #Pago total a pagar precio por cantidad. (Precio en Dollar)
        self.cantidad=int(input(f"Digta cantidad de Telefonos que quiere: "))
        assert self.cantidad>=1, f"Debe seleccionar al menos UN producto" #Validacion
        self.total=self.precio*self.cantidad
        return self.total

    def impuestos(self):
        #Estes es mi total de Impuesto a pagar.
        self.impuesto=self.total * Item.impuesto 
        self.precio_mas_impuesto=self.impuesto + self.total 
        return self.precio_mas_impuesto
    def envio_internacional(self):
        return self.precio_mas_impuesto + Item.envio
#Instancia 2   
telefono1=Item(100,"AXP123","Xiomi")
print(f"Modelo es {telefono1.modelo}")
print(f"Marca del telefono: {telefono1.marca}")
print(f"Pago total del telefono: {telefono1.Pago_total()}")
print(f"Pago de Impuestos del producto: {telefono1.impuestos()} pesos")
print(f"El precio de envio es de : {telefono1.envio_internacional()}")
print()
#Instancia 1
telefono2=Item(500,"13","Apple")
print(f"Modelo es {telefono2.modelo}")
print(f"Marca del telefono: {telefono2.marca}")
print(f"Pago total del telefono: {telefono2.Pago_total()}")
print(f"Pago de Impuestos del producto: {telefono2.impuestos()} pesos")
print(f"El precio de envio es de : {telefono2.envio_internacional()}")

from re import X


class Coordenada:
    
    def __init__(self,x,y) -> None:
        self.x=x 
        self.y=y

    def distancia(self, coordenada):
        x_diff=(self.x - coordenada.x )**2
        y_diff=(self.y - coordenada.y )**2

        return (x_diff + y_diff)**0.5




if __name__ == "__main__":
    cood_1=Coordenada(3,30)
    cood_2=Coordenada(4,8)

    print(cood_1.distancia(cood_2))
    #Metodo ins instance
    print(isinstance(cood_1,Coordenada)) #True. 
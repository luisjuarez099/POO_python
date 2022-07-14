print("Mi priemera linea de Busqueda lineal")
import random
def busqueda_lineal(lista,objetivo):
    global iterador 
    iterador+=1
    match = False;
    for i in lista:
        if i == objetivo:
            match = True
            break
    return match

if __name__=='__main__':
    tamano_lista=int(input("Digita tamano de la lista: "))
    objetivo=int(input("Que numero quires encontar: "))
    iterador =0
    lista=sorted([random.randint(0,100) for x in range(tamano_lista)])
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "No esta "} en la lista')

    print("Iteraciones numero: ",format(iterador))
    
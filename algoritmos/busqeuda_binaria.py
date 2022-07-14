print("Mi priemera linea de Busqueda lineal")
import random
def busqueda_binaria(lista,inicio,final,objetivo):
    global contador
    contador+=1
    print(f"Inicio {lista[inicio]} final {lista[final-1]}")
    if inicio> final:
        return False

    medio=(inicio + final)//2

    if lista[medio]==objetivo:
        return True
    elif lista[medio]<objetivo:
        return busqueda_binaria(lista, medio +1,final,objetivo)
    else:
        return busqueda_binaria(lista,inicio,medio-1,objetivo)

if __name__=='__main__':
    tamano_lista=int(input("Digita tamano de la lista: "))
    objetivo=int(input("Que numero quires encontar: "))
    contador=0
    lista=sorted([random.randint(0,100) for x in range(tamano_lista)])
    encontrado = busqueda_binaria(lista,0,len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "No esta "} en la lista')
    print(contador)

    
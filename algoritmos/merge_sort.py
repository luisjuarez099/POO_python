import random

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista)//2
        izq=lista[:medio]
        der=lista[medio:]

        #Llamada recurdiva
        merge_sort(izq)
        merge_sort(der)

        #iteradores para recorre rsublistas
        i=0
        j=0
        #iterador para la lista principal
        k=0

        while i<len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k]=izq[i]
                i+=1
            else:
                lista[k]= der[j]
                j+=1
            k+=1
        while i<len(izq):
            lista[k]= izq[i]
            i+=1
            k+=1
        while j< len(der):
            lista[k]=der[j]
            j+=1
            k+=1
    return lista



if __name__=='__main__':
    tamano_lista=int(input("Digita tamano de la lista: "))
    lista=[random.randint(0,100) for i in range(tamano_lista)]
    print('-'*20)
    lista_ordenada=merge_sort(lista)
    print(lista_ordenada)

import random


def generaLista():
    lista=[]
    for i in range(5):
        lista.append(random.randint(1,28))
    lista.sort()
    return lista


list=generaLista()
print(list)


fa = open("Ejercicio_Listas/archivo1.txt","w")
fa.write(str(list)  )
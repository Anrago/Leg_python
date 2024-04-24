import random


def generaLista():
    lista=[]
    for i in range(5):
        lista.append(random.randint(1,28))
    lista.sort()
    return lista

def escribirListasEnArchivoTXT(archivo,listas):
    archivo.write(str(listas))
    archivo.write("\n") 

fa = open("Ejercicio_Listas/Archivo1000Listas.txt","w")
for a in range(1000):
    lis=generaLista()
    escribirListasEnArchivoTXT(fa,lis)
fa.close()
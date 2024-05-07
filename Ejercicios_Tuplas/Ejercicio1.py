# Antonio Ramos Gonzalez
# Mt: 372576
# Ejercicio equipo TUPLAS
# 04/05/2024

"""Simulación del juego de datos Craps."""
import random
import matplotlib.pyplot as ptl
import numpy as np
import statistics as st

def lanzar_dado():
    """Lanza dos dados y regresa los valores de sus caras como una tupla."""
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    return (dado1, dado2) #empaqueta los valores de las caras de los dados en una tupla.

lanzamientos=int(input("Ingresa numero de juegos a simular: "))
gano=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
perdio=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lista_Duracion=[]
#determina el estado y puntaje del juego, basandose en el primer tiro
for n in range(lanzamientos):
    i=1
    FueraCiclo=False
    while FueraCiclo==False:
        valor_dado = lanzar_dado() #primer tiro
        suma_de_dados = sum(valor_dado)
        if suma_de_dados in (7, 11): #ganó
            estatus_juego = 'Ganó'
            if i<=12:
                gano[i]+=1
                lista_Duracion.append(i)
            else:
                gano[13]+=1
                lista_Duracion.append(i)
            FueraCiclo=True
            
        elif suma_de_dados in (2, 3, 12): #perdio
            estatus_juego = 'Perdio'
            if i<=12:
                perdio[i]+=1
                lista_Duracion.append(i)
            else:
                perdio[13]+=1
                lista_Duracion.append(i)
            FueraCiclo=True
        i+=1


        #Muestra el mensaje "Ganó" o "Perdio :|"
print("GANO: ",gano)
print("PERDIO: ",perdio)
Juegos=[gano,perdio]
indices=list(range(len(gano)))
prob_Ganar=list(range(len(gano)))
for i in range(1,len(gano)):
        prob_Ganar[i]=(gano[i]/lanzamientos)


print("PROBABILIDAD DE GANARA A LOS DADOS: ",sum(gano)/lanzamientos)
print("MEDIA DURACION DE LOS JUEGOS: ",np.mean(lista_Duracion))
print("MEDIANA DURACION DE LOS JUEGOS: ",np.median(lista_Duracion))
print("MODA DURACION DE LOS JUEGOS: ",st.mode(lista_Duracion))
print("PROBABILIDADES DE GANAR: ", prob_Ganar[1::])



fig,ax=ptl.subplots()
ax.barh(indices,gano,color="green")
ax.barh(indices,perdio,color="red", left=gano)
ptl.xlabel("No. Juegos")
ptl.ylabel("No. Lanzamientos")
ptl.show()
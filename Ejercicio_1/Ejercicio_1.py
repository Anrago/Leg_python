"""
Antonio Ramos Gonzalez
Matricula.-372576
Ejercicios I
20/02/2024
"""

import math

# Ejercicio 1.1
print("\n\n EJERCICIO 1.1")
x=2
y=3

print("X = ", x)
print('Value of', x, '+', x, 'is', (x + x))
print("X =")
print((x+y),'x = ',(y+x))

# Ejercicio 1.2
print("\n\n EJERCICIO 1.2")
#incorrecto
#Calificaion=input("Ingrese una calificacion entre 1 y 100 ")

#Correcto
Calificacion=int(input("Ingrese una calificacion del 1 al 100 "))

# EJERCICIO 1.3
print("\n\n EJERCICIO 1.3")
if Calificacion >= 90:
    print("Felicidades Tu calificacion de ",Calificacion," Te otorga una A en este curso")


# EJERCICIO 1.4
print("\n\n EJERCICIO 1.4")
radio=2

print("Radio: ",radio)
print("PI: ",math.pi)
print("Diametro",radio*2)
print("Circunferencia: ",(2*math.pi)*radio)
print("Area: ",(math.pi)*(radio**2))

# EJERCICIO 1.5
print("\n\n EJERCICIO 1.5")
numero=int(input("ingrese numero para saber si es par o impar: "))

if (numero%2)==0:
    print("El numero entero ",numero," es par")
if (numero%2)!=0:
    print("El numero entero ",numero," es impar")

# Ejercicio 1.6
print("\n\n EJERCICIO 1.6")
PrimerNumero=int(input("Ingrese el primer entero: "))
Multiplo=int(input("ingresa el segundo entero: "))
if PrimerNumero>Multiplo:
    if PrimerNumero%Multiplo==0:
        print(Multiplo," es multiplo de ",PrimerNumero)

    if PrimerNumero%Multiplo!=0:
        print(Multiplo," no es multiplo de ",PrimerNumero)
        
if PrimerNumero<Multiplo:
    if Multiplo%PrimerNumero==0:
        print(PrimerNumero," es multiplo de ",Multiplo)

    if Multiplo%PrimerNumero!=0:
        print(PrimerNumero," no es multiplo de ",Multiplo)

# Ejercicio 1.7
print("\n\nEJERCICIO 1.7")
print("numero\t","cuadrado","cubo")
print(1,"\t",1**2,"\t ",1**3)
print(2,"\t",2**2,"\t ",2**3)
print(3,"\t",3**2,"\t ",3**3)
print(4,"\t",4**2,"\t ",4**3)
print(5,"\t",5**2,"\t ",5**3)

# Ejercicio 1.8
print("\n\n EJERCICIO 1.8")
print("numero\t","cuadrado","cubo")
print(f"1 \t {1**2} \t  {1**3:4d}")
print(f"2 \t {2**2} \t  {2**3:4d}")
print(f"3 \t {3**2} \t  {3**3:4d}")
print(f"4 \t {4**2} \t  {4**3:4d}")
print(f"5 \t {5**2} \t  {5**3:4d}")


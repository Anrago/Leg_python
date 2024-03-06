#Nombre: Antonio Ramos Gonzalez
#Mt: 372576
#Actividad: Practica 4 while
#Fecha: 06/03/2024
i=1

print("Decendente")
while i<=5:
    if i!=5:
        print(f"{i},")
    else:
        print(f"{i}")
    i+=1;

i=5

print("Decendente")
while i>=1:
    if i!=1:
        print(f"{i},")
    else:
        print(f"{i}")
    i-=1

print("Horizontal asc")
cad=''
i=1
while i<=5:
    if i!=5:
        cad=cad+str(i)+','
    else:
        cad=cad+str(i)
    i+=1;
print(cad)
print("\nHorizontal des")
i=5
cad=''
while i>=1:
    if i!=1:
        cad=cad+str(i)+','
    else:
        cad=cad+str(i)
    i-=1
print(cad)

print('\n')
num=int(input("\nIngresa un numero para la sumatoria: "))

sum=0
i=0

while i<=num:
    sum+=i
    i+=1

print(sum)


print("CORAZONES")
renglon=0
maximo_renglon=10
maximo_columna=16
cadena_renglon=''

while renglon<maximo_renglon:
    columna=0
    while columna<maximo_columna:
        cadena_renglon=cadena_renglon + '♥' +''
        columna+=1
    cadena_renglon=cadena_renglon + '\n'
    renglon+=1
print(cadena_renglon)

print("NUMBRE ENCERRADO")
nombre=input("Ingrese nombre: ")
caracter=input("Ingrese caracter: ")
cant=len(nombre)
simb=''
i=0
while i<=cant:
    simb=simb+caracter
    i+=1;
print(simb+caracter)
print(caracter+nombre+caracter)
print(simb+caracter)


print("PRISMA")
num=int(input("Ingrese numero impar: "))
caracter=input("Ingrese caracter")


cad=''

if num%2==0:
    print("El numero es par")
else:
    i=1
    sp=num//2
    while i<=num:
        print(" " * sp + caracter * i)
        i+=2
        sp-=1
    i-=4
    sp=1
    while i>0:
        print(" " * sp + caracter * i)
        i-=2
        sp+=1
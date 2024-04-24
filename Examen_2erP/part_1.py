#Antonio Ramos Gonzalez
#Matricula:372576
#2do examen parcial: pate 1
#9/04/2024
longitud = int(input('Ingrese un numero par para establecer la longitud horizontal de la base del triangulo: '))
caracter = input('Ingrese el caracter que imprimira el triangulo: ')

cadena_triangulo=''
numero_espacio=longitud//2
numero_caracter=1

renglon_parte1=0
for renglon_parte1 in range(numero_espacio): 
    columna = 0
    numero_caracter_renglon=numero_espacio+numero_caracter
    for columna  in range(numero_caracter_renglon):
        if columna<numero_espacio:
                cadena_triangulo=cadena_triangulo+' '
        else:
            cadena_triangulo=cadena_triangulo+caracter
    numero_caracter = numero_caracter +2
    numero_espacio= numero_espacio -1
    cadena_triangulo = cadena_triangulo +'\n'


renglon_parte2=0
for renglon_parte2 in range(longitud):

    cadena_triangulo = cadena_triangulo+caracter
    
cadena_triangulo=cadena_triangulo+'\n'

print(cadena_triangulo)






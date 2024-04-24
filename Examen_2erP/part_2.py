#Antonio Ramos Gonzalez
#Matricula:372576
#2do examen parcial: pate 2 
#9/04/2024
apro=0
repro=0
cal=0

total=0
while cal != -1:
    cal = int(input('Ingrese la calificacion, -1 para terminar: '))
    if cal > 100 or cal<0 & cal == -1:
        print('La calificacion esta fuera del rango, porfavor ingresar una calificacion entre 0 y 100')
    else:
        if cal != -1:
            if cal < 60:
                repro+=1
            else:
                apro+=1
            total+=cal
print()

if total==0:
    print('No se ingresaron calificaciones')
else:
    print('Promedio de las calificaciones capturadas del 2do examen parcial: ',int(total/(repro+apro)))
    print('Cantidad de alumnos reprobados en el 2do examen parcial: ',repro)
    print('Cantidad de alumnos aprobados en el 2do examen parcial: ',apro)
    if total/(repro+apro)>=90:
        print('El docente obtuvo un buen desempenio en el segundo parcial')
    else:
        print('El docente no obtuvo un buen desempenio en el segundo parcial')

    

total=0;

count=0;

cal=int(input("INGRESA PRIMERA CALIFICACION: "))

while cal!=-1:
    total+=cal
    count+=1
    cal=int(input("INGRESA SIGUIENTE CALIFICACION: "))

if count!=0:
    prom=total/count
    print(prom)
else:
    print("NO SE HA INGRESADO NINGUNA CALIFICACION")


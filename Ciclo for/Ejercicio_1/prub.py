#n= int(input("INGRESA NUMERO: "))
#
#
#if n%2==0:
#    print("ESTE NUMER ES PAR")
#else:
#    print("ESTE NUMERO ES IMPAR")
#
#n= int(input("INGRESA NUMERO 1: "))
#y= int(input("INGRESA NUMERO 2: "))
#
#if n>y:
#    if n%y==0:
#        print(y," :SON MULTIPLOS: ",n)
#    else:
#        print(y," :NO SON MULTIPLOS: ",n)
#else:
#    if y%n==0:
#        print(n," :SON MULTIPLOS: ",y)
#    else:
#        print(n," :NO SON MULTIPLOS: ",y)
#
#n= int(input("INGRESA NUMERO: "))
#y= int(input("INGRESA NUMERO: "))
#z= int(input("INGRESA NUMERO: "))
#
#if n==y==z:
#    print("SON IGUALES")
#else:
#    print("SON DIFERENTES")

calificacion=int(input("INGRESA CALIFICACION: "))

if calificacion>=70:
    if calificacion>=80:
        if calificacion>=90:
            print("TU CALIFICACION ES A")
        else:
            print("TU CALIFICACION EN B")
    else:
        print("TU CALIFICACION ES C")
else:
    if calificacion >=60:
        print("TU CALIFICACION ES D")
    else:
        print("TU CALIFICACION ES F")

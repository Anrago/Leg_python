#Antonio Ramos Gonzalez
#matricula:372576
#Primera parte primer Examen
#5/3/2024
num1 = int(input("Ingresa numero 1 entero: "))
num2 = int(input("Ingresa numero 2 entero: "))
num3 = int(input("Ingresa numero 3 entero: "))
cont=0;
cont_Igual=0


if(num1==num2):
    if(num1==num3):
        print(f"los valores {num1}, {num2}, {num3} son iguales")
        cont_Igual=1;
    if(num1!=num3):
        print(f"los valores {num1}, {num2}, {num3}  no son iguales")
        cont=1
if(num2!=num3):
    if(cont==0):
        print(f"los valores {num1}, {num2}, {num3}  no son iguales")



if(cont_Igual==0):
    if(num1>=num2):
        if(num3>=num1):
            print(f"El orden de los numeros de forma descendente {num3}, {num1}, {num2}")
        if(num3<=num1):
            if(num2>=num3):
                print(f"El orden de los numeros de forma descendente {num1}, {num2}, {num3}")
                cont=1;
            if(cont==0): 
                if(num2<=num3):
                    print(f"El orden de los numeros de forma descendente {num1}, {num3}, {num2}")
        cont=1;
if(cont==0):
    if(num2>=num1):
        if(num3>=num2):
            print(f"El orden de los numeros de forma descendente {num3}, {num2}, {num1}")
        if(num3<=num2):
            if(num1>=num3):
                print(f"los numero en orden descendente : {num2}, {num1}, {num3}")
                cont=1;
            if(cont==0):
                if(num1<=num3):
                    print(f"El orden de los numeros de forma descendente {num2}, {num3}, {num1}")
if(cont_Igual==1):
    print("Los numeros son iguales, por lo que no hay necesidad de mostrar su orden")
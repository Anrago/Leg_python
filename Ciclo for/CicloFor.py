#Antonio Ramos Gonzalez
#Mt: 372576
#16/03/2024
#Ciclo for
#-----------------------EJERCICIO 30----------------------------
bac=0
print("Horas \t No.Bacterias")
for horas in [0,5,10,15]:
    bac=200*(2**int(horas))
    print(horas,"\t",bac)
    
print("\n fstrings")
print(f"Horas \t No.Bacterias")
for horas in [0,5,10,15]:
    bac=200*(2**int(horas))
    print(f"{'':<4}{horas:<15}{bac}")

#-----------------------EJERCICIO 31----------------------------

seg=int(input("INGRESE NUMERO DE SEGUNDOS: "))

segRe=seg%60
min=seg/60
hora=min/60

if min>=60:
    min-=60

print(int(hora),"-",int(min),"-",segRe)

#-----------------------EJERCICIO 32----------------------------

seg=int(input("(Bucle)INGRESE NUMERO DE SEGUNDOS: "))
cad=[0,0,0];
i=0
for c in [3600,60,1]:
    cad[i]=cad[i]+(seg//c)
    i+=1
print("Horas",cad[0],"Min",cad[1]%60,"seg",cad[2]%60)

#-----------------------EJERCICIO 33----------------------------

perfect=int(input("Ingrese numero positivo entero para saber si es perfecto: "))
yes=0
for i in range(1,perfect):

    if perfect%i==0:
        yes+=i
if yes==perfect:
    print("El numero ",perfect," es un numero perfecto")
else:
    print("El numero ",perfect," no es un numero perfecto")

#-----------------------EJERCICIO 34----------------------------

binario=int(input("INGRESE NUMERO EN BINARIO(0 y 1): "))
temp=binario
decimal = 0
posicion = 0
for _ in range(len(str(binario))):
    des = temp % 10
    decimal += des * (2 ** posicion)
    temp //= 10
    posicion += 1

print("El numero binario ",binario," en decimal es: ", decimal)

#-----------------------EJERCICIO 35----------------------------

decimal=int(input("INGRESE NUMERO EN DECIMAL: "))
temp=decimal
binario = 0
posicion = 1
for _ in range(len(str(decimal))):
    bin = temp % 2
    binario += bin * posicion
    temp //= 2
    posicion *= 10

print("el numero entero decimal ",decimal," en binario es: ", binario)
    
#-----------------------EJERCICIO 36----------------------------

capicua=str(input("Ingresa numero para determinar si es capicua"))
i=len(capicua)-1
temp=0
for c in capicua:
    if c != capicua[i]:
        temp+=1
    i-=1
if temp==0:
    print("El numero ",capicua," no es capicua")
else:
    print("El numero ",capicua," no es capicua")

#-----------------------EJERCICIO 37----------------------------

palindromo=str(input("INGRESA UNA FRASE PARA DETERMINAR SI ES UN PALINDROMO: "))
temp=0
cad=""

for c in palindromo:
    if c!=" ":
        cad=cad+c

i=len(cad)-1
print(cad)
for c in cad:
    if c!=cad[i]:
        temp+=1
    i-=1
if temp==0:
    print("La frase ",palindromo," si es palindromo")
else:
    print("La frase ",palindromo," no es palindromo") 
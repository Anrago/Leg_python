#Antonio Ramos Gonzalez
#Matricula.-372576
#Ejercicios 1.9 --- 1.17
#21/02/2024
import sys
print(" EJERCICIO 1.9")
print(f"""B={ord('B')}\nC={ord('C')}\nD={ord('D')}\nb={ord('b')}\nc={ord('c')}\nd={ord('d')}
0={ord('0')}\n1={ord('1')}\n2={ord('2')}\n$={ord('$')}\n*={ord('*')}\n+={ord('+')}""")



#EJERCICIO 10

print("\n\n EJERCICIO 1.10")
primerNumero=int(input("Ingrese el primer numero: "))
segundoNumero=int(input("Ingrese el segundo numero: "))
tercerNumero=int(input("Ingrese el tercer numero: "))
suma=primerNumero+segundoNumero+tercerNumero
print(f"""La suma de los numeros {primerNumero},{segundoNumero},{tercerNumero} es: {suma}""")
print(f"""El promedo de los numeros {primerNumero},{segundoNumero},{tercerNumero} es: {suma/3}""")
print(f"""El producto de los numeros {primerNumero},{segundoNumero},{tercerNumero} es: {primerNumero*segundoNumero*tercerNumero}""")
if primerNumero>segundoNumero:
    if primerNumero>tercerNumero:
        print("El mayor de los numeros es:  ",primerNumero)
    if primerNumero<tercerNumero:
        print("El mayor de los numeros es:  ",tercerNumero)
if segundoNumero>primerNumero:
    if segundoNumero>tercerNumero:
        print("El mayor de los numeros es:  ",segundoNumero)
    if segundoNumero<tercerNumero:
        print("El mayor de los numeros es:  ",tercerNumero)

if primerNumero<segundoNumero:
    if primerNumero<tercerNumero:
        print("El menor de los numeros es: ",primerNumero)
    if primerNumero>tercerNumero:
        print("El menor de los numeros es: ",tercerNumero)
if segundoNumero<primerNumero:
    if segundoNumero<tercerNumero:
        print("El menor de los numeros es: ",segundoNumero)
    if segundoNumero>tercerNumero:
        print("El menor de los numeros es: ",tercerNumero)


print("\n\n EJERCICIO 1.11")
Digitos=int(input("Ingrese un numero de 5 digitos: "))
print(f"{Digitos//10000}   {(Digitos%10000)//1000}   {(Digitos%1000)//100}   {(Digitos%100)//10}   {Digitos%10}")

print("\n\n EJERCICIO 1.12")
p=100000
r=0.07
print(f"""La rentabilidad de 7% de sus 100,000 a 1 anio es: {p*((1+r)**1)-100000}""")
print(f"""La rentabilidad de 7% de sus 100,000 a 2 anio es: {p*((1+r)**2)-100000}""")
print(f"""La rentabilidad de 7% de sus 100,000 a 3 anio es: {p*((1+r)**3)-100000}""")


print("\n\n EJERCICIO 1.13")
sys.set_int_max_str_digits(10000)
print(5**14284)

print("\n\n EJERCICIO 1.14")
ultimoDigito=int(input("Ingrese un numero para regresar el ultimo digito: "))
print(f"El ultimo digito de {ultimoDigito} es {ultimoDigito%10}")

print("\n\n EJERCICIO 1.15")

primerNumero=float(input("Ingrese el primer numero: "))
segundoNumero=float(input("Ingrese el segundo numero: "))
tercerNumero=float(input("Ingrese el tercer numero: "))

if primerNumero<segundoNumero:
    if primerNumero<tercerNumero:
        print("El menor de los numeros es: ",primerNumero)
    if primerNumero>tercerNumero:
        print("El menor de los numeros es: ",tercerNumero)
if segundoNumero<primerNumero:
    if segundoNumero<tercerNumero:
        print("El menor de los numeros es: ",segundoNumero)
    if segundoNumero>tercerNumero:
        print("El menor de los numeros es: ",tercerNumero)

print("\n\n EJERCICIO 1.16")

primerNumero=float(input("Ingrese el primer numero: "))
segundoNumero=float(input("Ingrese el segundo numero: "))
tercerNumero=float(input("Ingrese el tercer numero: "))

if primerNumero==segundoNumero:
    if primerNumero==tercerNumero:
        print(f"Los numeros {primerNumero}, {segundoNumero}, {tercerNumero} son iguales")
    if primerNumero!=tercerNumero:
        print(f"Los numeros {primerNumero}, {segundoNumero}, {tercerNumero} son diferentes")
if segundoNumero!=primerNumero:
    print(f"Los numeros {primerNumero}, {segundoNumero}, {tercerNumero} son diferentes")


print("\n\n EJERCICIO 1.17")

primerNumero=float(input("Ingrese el primer numero: "))
segundoNumero=float(input("Ingrese el segundo numero: "))
tercerNumero=float(input("Ingrese el tercer numero: "))

if primerNumero < segundoNumero:
    if segundoNumero < tercerNumero:
        print("El orden de sus numeros es",primerNumero,segundoNumero,tercerNumero)
if primerNumero < tercerNumero:
    if tercerNumero < segundoNumero:
        print("El orden de tus numeros son",primerNumero, tercerNumero,segundoNumero)

if segundoNumero < primerNumero:
    if primerNumero < tercerNumero:
        print("El orden de sus numeros es",segundoNumero,primerNumero, tercerNumero)
if segundoNumero < tercerNumero:
    if tercerNumero < primerNumero:
        print("El orden de tus numeros son",segundoNumero, tercerNumero,primerNumero)

if tercerNumero < primerNumero:
    if primerNumero < segundoNumero:
        print("El orden de sus numeros es", tercerNumero,primerNumero,segundoNumero)
if tercerNumero < segundoNumero:
    if segundoNumero < primerNumero:
        print("El orden de tus numeros son", tercerNumero,segundoNumero,primerNumero)

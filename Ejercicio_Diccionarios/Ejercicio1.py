import os
import platform

system=platform.system()

def clear():
    if system == "Linux":
        os.system("clear")
    if system == "Windows":
        os.system("cls")

def pause():
    if system == "Linux":
        input("Ingrese una tecla para continuar...")
    elif system == "Windows":
        os.system("pause")



def Buscar(Alumnos):
    matBus=int(input("Ingrese matricula a buscar: "))

    if matBus in Alumnos:
        nom=Alumnos[matBus]
        print("NOMBRE DEL ALUMNO: ",nom)
    else:
        print("Alumno no encontrado")

def Mostrar(Alumnos):
    for mat,nom in Alumnos.items():
        print("Mat:",mat,"| Nombre: ",nom)

        

def eliminarAlumno(Alumnos):
    mat = int(input("INGRESA MATRICULA DE ALUMNO A ELIMINAR: "))
    if mat in Alumnos:
        del(Alumnos[mat])
        print("Alumno Eliminado con exito")
    else:
        print("Alumno no encontrado")




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




def IngresarAlumno():
    Nombre=input("INGRESA NOMBRE DEL ALUMNO: ")
    Mat=int(input("INGRESA MATRICULA: "))
    return Mat,Nombre

Alumnos={}
while True:
    clear()
    print("MENU")
    print("1.-Ingresar Alumno")
    print("2.-Buscar Alumno")
    print("3.-Imprimir Registro")
    print("4.-Eliminar Alumno")
    print("5.-Salir")
    opc=int(input("Ingresa un opcion: "))
    if opc == 1:
        clear()
        Mat,Nombre=IngresarAlumno()
        Alumnos[Mat]=Nombre
    if opc == 2:
        clear()
        Buscar(Alumnos)
        pause()
    if opc == 3:
        clear()
        Mostrar(Alumnos)
        pause()
    if opc == 4:
        clear()
        eliminarAlumno(Alumnos)
        pause()


        
        

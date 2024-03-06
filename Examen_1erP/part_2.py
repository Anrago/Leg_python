#Antonio Ramos Gonzalez
#matricula:372576
#Segunda parte primer Examen
#5/3/2024
huevos=int(input("Ingresa cantidad de huevos: "))
cartera=6
sobrante=0
entrada=int(huevos/6);
if(huevos>=cartera):
    sobrante=(huevos-cartera)
    if(sobrante%6==0):
        print(f"Cantidad de carteras llenas: {entrada}")
    if(sobrante%6!=0):
        print(f"Se llenanaron {int(entrada)} de 6 huevos")
        print(f"En la ultima cartera se colocaron {int(huevos-(entrada*cartera))}")
        print(f"La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de: {cartera-(int(huevos-(entrada*cartera)))}")
if(huevos<cartera):
    sobrante=(huevos-cartera)
    if (huevos==0):
        print("La cantidad de huevos necesarios para llenar una cartera es: 6")
    if (huevos!=0):
        print(f"La cantidad de huevos necesarios para llenar una cartera es: {cartera-huevos}")
        print(f"En la ultima cartera se colocaron {int(huevos-(entrada*cartera))}")
        print(f"La cantidad de huevos adicionales que se necesitan para llenar la ultima cartera es de: {cartera-(int(huevos-(entrada*cartera)))}")
        
        

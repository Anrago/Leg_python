import random

def lanzarDado():
    valor1=random.randint(1,6)
    valor2=random.randint(1,6)
    return valor1, valor2
    
def mostrarDados(dado):
    print(f"El valor de tus dados son {dado[0]} y {dado[1]}, dando un total de: {dado[0]+dado[1]}")
    

dados=lanzarDado()

mostrarDados(dados)

suma = dados[0] + dados[1]
ant=0
n=0
while True:
    if suma==7 or suma== 11 and n==0:
        print("Felizaidades has ganado papupro")
        break
    elif suma == 2 or suma==3 or suma==12 and n==0:
        print("Perdiste papu, la casa")
        break
    elif suma==1 or suma==4 or suma==5 or suma==6 or suma==8 or suma==9 or suma==10:
        print("El juego continua papu")
        ant=suma
        dados=lanzarDado()
        mostrarDados(dados)
        suma = dados[0] + dados[1]

    if ant == suma and n==1:
        print("FELIZIDADES GANASTE EN LA SIGUIENTE VUELTA")
        break
    else:
        print("Perdiste papu, la casa")
        break
    n+=1
    



        
        

            
        
        

        
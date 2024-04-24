import random

def lanzarDado():
    valor1=random.randint(1,6)
    valor2=random.randint(1,6)
    return valor1, valor2
    
def mostrarDados(dado):
    print(f"El valor de tus dados son {dado[0]} y {dado[1]}, dando un total de: {dado[0]+dado[1]}")
    

dados=lanzarDado()

saldo=1000
apuesta=0
opc=''

suma = dados[0] + dados[1]
ant=0
n=0
while True:
    print()
    print("Saldo actual: ",saldo)
    apuesta = int(input("INGRESA CANTIDAD A APOSTAR: "))
    opc = input("Escribe lanzar para lanzar dado: ")
    if opc=='lanzar' and saldo!=0 and apuesta<saldo:
        mostrarDados(dados)
        if suma==7 or suma== 11:
            print("Felizaidades has ganado papupro")
            saldo+=apuesta
            continue
            
        elif suma == 2 or suma==3 or suma==12:
            print("Perdiste papu, la casa")
            saldo-=apuesta
            continue
            
        elif suma==1 or suma==4 or suma==5 or suma==6 or suma==8 or suma==9 or suma==10:
            print("El juego continua papu")
            ant=suma
            dados=lanzarDado()
            suma = dados[0] + dados[1]
            continue

        if ant == suma and n==1:
            print("FELIZIDADES GANASTE EN LA SIGUIENTE VUELTA")
            saldo+=apuesta
            continue
            
        else:
            print("Perdiste papu, la casa")
            saldo-=apuesta
            continue
            
        n+=1
    elif saldo!=0 and apuesta>saldo:
        print("Saldo insuficiente")
    elif opc=='retirar':
        break
    
    



        
        

            
        
        

        
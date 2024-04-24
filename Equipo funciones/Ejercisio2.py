from itertools import combinations

def GenNumber(Ri,Rf,Cant):
    
    lista=[0]
    for n in range(Ri,Rf):
        lista[n]=n
    combinations(lista,Cant)
    return lista

def ImprimirCombinaciones(combinaciones):
    print("Combinaciones: ")
    x=1
    for n in combinaciones:
        print(f"Combinacion {x}: {n}")
        x+=1
    


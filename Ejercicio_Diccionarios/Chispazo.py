# Antonio Ramos Gonzalez
# Matricula:372576
# 10/05/2024
# Expo Diccionarios: Chispazo

def CombCont(Nombrefa):
    CombGrupo = {}

    with open(Nombrefa, 'r') as fa:
        for idx,line in enumerate(fa, start=1):
            Grupos = line.strip().split()

            for i, grupo in enumerate(Grupos, start=1):
                comb = CombGrupo.setdefault(f'{i}', {})
                CombInd = ' '.join(grupo.split()[:5])  
                comb[CombInd] = comb.get(CombInd, 0) + 1

    return CombGrupo

resultado = CombCont('GandoresChispazo.txt')

for grupo, comb in resultado.items():
    print(f'Combinaciones del grupo {grupo}:')
    for comb, cont in comb.items():
        print(f'{comb}.- {cont}')
    print()


def CopiasProfe(examenes,k):
    C_profe = 0 
    Memoria = []
    for i in range(len(examenes)):
        b = i
        if i<=k:
            a=0
        else:
            a+=1
        Memoria = examenes[a:b]
        if examenes[i] in Memoria:
            C_profe+=1
    return C_profe





def CopiasTotales(examenes):
    Copias2 = []
    Copias = len(examenes)-len(set(examenes))
    for i in range(len(examenes)):
        if Copias2.count(examenes[i]) == 0:
            Copias2.append(examenes[i])
    C_totales = len(examenes) - len(Copias2)
    return C_totales, Copias, Copias2




def LeerDatos():
    N,K = input().split() #leer los valores de n y k
    examenes = list(map(int,input().split())) # Volver una lista una serie de datos ingresados
    return int(N), int(K), examenes


def principal():
    N,k,examenes = LeerDatos()
    a,b,c = CopiasTotales(examenes)
    d = CopiasProfe(examenes,k)
    print(a,b,c,d)

principal()
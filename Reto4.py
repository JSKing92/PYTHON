
N = int(input("Cantidad de datos"))
K = int(input("Cantidad de memorizables"))
datos_crudos = input('Dime los numeros: ')
Arreglo = [float(d) for d in datos_crudos.split()]
Index1 = list(range(N))
Index2 = list(range(K))
Index3 = list(range(K,N))
Copiados = []
Copiados2 = []
print(Index1)
print(Arreglo)
J=0
S=0

for i in Index1:
    if Arreglo.count(Arreglo[i]) > 1 and Copiados.count(Arreglo[i])==0:
        Copiados.append(Arreglo[i])
        J=J+Arreglo.count(Arreglo[i])-1

for i in Index2:
    if Arreglo.count(Arreglo[i]) > 1 and Copiados2.count(Arreglo[i])==0:
        Copiados2.append(Arreglo[i])
        S=S+Arreglo.count(Arreglo[i])-1

for i in Index3:
    if (Arreglo[i-K:i].count(Arreglo[i])>1):
        S=S+1


        
print(J)
print(Index2)
print(Index3)
print(Copiados)
print(S)
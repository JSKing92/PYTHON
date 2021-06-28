N, K = input().split()
a=int(N)
b=int(K)
datos_crudos = input()
Arreglo = [float(d) for d in datos_crudos.split()]
Index1 = list(range(a))
Index2 = list(range(b))
Index3 = list(range(b,a))
Copiados = []
Copiados2 = []

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
    if (Arreglo[i-b:i].count(Arreglo[i])>1):
        S=S+1


        
print(J,S)

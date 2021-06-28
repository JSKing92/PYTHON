N, K = input().split()
a=int(N)
b=int(K)
datos_crudos = input()
Arreglo = [float(d) for d in datos_crudos.split()]
Index1 = list(range(a))
Index2 = list(range(b+1))
Index3 = list(range(b+1,a))
Copiados = []
Copiados2 = []

J=0
S=0
r=0

for i in Index1:
    if Arreglo.count(Arreglo[i]) > 1 and Copiados.count(Arreglo[i])==0:
        Copiados.append(Arreglo[i])
        J=J+Arreglo.count(Arreglo[i])-1

for i in Index2:
    if Arreglo[0:b+1].count(Arreglo[i]) > 1 and Copiados2.count(Arreglo[i])==0:
        Copiados2.append(Arreglo[i])
        S=S+Arreglo[0:b+1].count(Arreglo[i])-1

for i in Index3:
    print(Arreglo[i-b:i+1])
    if (Arreglo[i-b:i+1].count(Arreglo[i])>1):
        print(Arreglo[i-b:i+1].count(Arreglo[i]))
        r=r+1


print(r)        
print(J,S+r)
print(Arreglo[0:b])
print(Index2)
print(Index3)
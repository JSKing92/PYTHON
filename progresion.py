ptermino = int(input("ingrese primer termino"))
diferencia = int(input("ingrese la diferencia"))
cota = int(input("ingrese la cota"))

numeros=[]
index = list(range(cota))
suma=0
numeros.append(ptermino)
for i in range(ptermino,cota+1,diferencia):
    suma = suma + i
    
for i in range(cota):
    value = numeros[i-1]+diferencia
    if value<= cota:
      numeros.append(value)

print(suma)

print(numeros)
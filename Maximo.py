




datos_crudos = input('Digite los nunmeros del arreglo separaso por un espacio: ')
Arreglo = [float(d) for d in datos_crudos.split()]
print(Arreglo)
k=0
def maximo(Arreglo,a,b):
 Max = 0 
 for i in range(a,b):
         for j in range(a,b):
            if Arreglo[j]>=Arreglo[i] and Arreglo[j]>Max:
                Max = Arreglo[j]
 print("El valor maximo entre la posicion ",a," y la posicion ",b," es: ",Max)

     

a = int(input("Ingrese la posicion infeior de izquierda a derecha empezando por 1: "))
b = int(input("Ingrese la posicion superior de izquierda a derecha empezando por 1: "))

if (b <= a):
    print("La posicion superior no puede ser menor o igual a la inferior ")

maximo(Arreglo,a,b)
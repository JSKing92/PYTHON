
i = int(input("Ingrese el nivel arrancando en 1, i: "))
j = int(input("Ingrese la posicion de izquierda a derecha arrancando en 1, j: "))
def triangulo(filas,Posicion):
    fila = [1]
    cero = [0]
    k = 0
    for i in range(filas):
        k=k+1
        fila = [i+d for i, d in zip(fila + cero, cero + fila)]
        if k == filas-1:
           print("El valor en el nivel: ",filas," En las posicion: ",Posicion," Es: ",fila[Posicion-1])

      

triangulo(i,j)
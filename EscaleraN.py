

n = int(input("Ingrese el numero de escalones: "))

index = list(range(n))
funcion = [1,2,3,5]

def Posibilidades(n):
    if n < 5 : 
        print("Para una escalera con ",n," escalones, se tienen: ",funcion[n-1]," Posibilidades")
    else:
        k=0
        for i in list(range(5,n+1)):
            k = funcion[i-2]+funcion[i-3]
            funcion.append(k)
            if i == n :
                print("Para una escalera con ",n," escalones, se tienen: ",funcion[n-1]," Posibilidades")

        


Posibilidades(n)
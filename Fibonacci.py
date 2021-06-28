
#Solicitamos el valor de n
n = int(input("Ingresa el valor de N: "))

#Creamos la funcion  
def Fibonacci (n):
 index = list(range(2,n+1))
 fibonacci = []
 fibonacci.append(1)
 fibonacci.append(1)

 for i in index:
    fi = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(fi)
 print('f(',n,') = ',fibonacci[n])

#llamamos la funcion pasandole como argumento el n del usuario
Fibonacci(n)

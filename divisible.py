numero1 = int(input("ingrese limite inferior"))
numero2 = int(input("ingrese limite superior"))
rango= list(range(numero1,numero2))
k=0

while k==0:
    for i in range(numero1,numero2+1):
        if (i%2==0 and i%3==0 and i%5==0):
            k=k+1
            print(i)
  
while numero1 <= numero2:
    if (numero1%2==0 and numero1%3==0 and numero1%5==0):
        print(numero1)
        break
    numero1=numero1+1


cadena = "Pensamos demasiado y sentimos muy poco"

cadena = cadena.lower()

letra = input("Introduce una letra")
valor = int(input("Introduce un valor"))
letra = letra.lower()
contador = 0
for i in cadena:
    if contador >= valor:
        print("\nSe ha superado el numero maximo")
        break
    if i==letra:
        contador+=1
    elif i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
          continue
    print(i, end=' ')
     



    
  
    



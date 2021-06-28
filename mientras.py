cadena = 'El pato hace quack'
cadena = cadena.lower()
print(cadena)
print(len(cadena))
vocales = 0
posicion = 0

while posicion < 18:
    if(cadena[posicion]=='a' or cadena[posicion]=='e' or cadena[posicion]=='i' or cadena[posicion]=='o' or cadena[posicion]=='u' ):
        vocales = vocales+1
    posicion=posicion+1

print(vocales, "Ejecutado con exito2")
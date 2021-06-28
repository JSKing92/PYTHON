
cadena = "Predecir el futuro resulta ser un negocio muy dificil en si"
cadena = cadena.lower()
print(cadena)
indice=0
letra = input("ingrese la letra")
texto = []

while indice< len(cadena):
    
    if (cadena[indice]==letra):
        texto.append("")
    else:
        texto.append(cadena[indice])
    indice=indice+1

print(texto)

for valor in cadena:
    if valor == letra:
        continue
    else:
        print(valor, end="")
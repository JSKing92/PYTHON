cantidad = float(input("Cantidad"))
interes = float(input("Interes"))
Anual = float(input("Numero de años"))

Capital = cantidad*(1+(interes/100))**Anual
print(Capital)
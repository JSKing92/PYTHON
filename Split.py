from statistics import variance
datos_crudos = input('Dime los numeros: ')
lista_datos = [float(d) for d in datos_crudos.split()]
print(variance(lista_datos))


def agregar(nproductos, nitems):
    if nitems[0] in nproductos:
        return False
    else: 
        i = nitems[0]
        nitems.pop(0)
        nproductos[i]=nitems
    print(nproductos)




productos = {1:["Manzanas", 2500.0,25],2:["Limones",3600.0,30]}

Accion = input("Ingrese la accion")
item = input().split()
item[0] = int(item[0])
item[2] = float(item[2])
item[3] = int(item[3])

agregar(productos,item)
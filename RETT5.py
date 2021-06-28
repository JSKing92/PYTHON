productos = {1:['Manzanas',8000.0,550,0],
             2:["Limones",2300.0,15,0],
             3:["Peras",2500.0,38,0],
             4:["Arandanos",9300.0,55,0],
             5:["Tomates",2100.0,42,0],
             6:["Fresas",4100.0,33,0],
             7:["Helado",4500.0,41,0],
             8:["Galletas",500.0,833,0],
             9:["Chocolates",3900.0,999,0],
             10:["Jamon",17000.0,10,0]}

def Calc(productos):
  s=0
  w=0
  r=0
  t=1000000000000
  for i in index:
    productos[i][3]=productos[i][2]*productos[i][1]
    s=s+productos[i][3]
    w=w+productos[i][1]

  for i in index:
    for j in index:
        if(productos[j][1]>productos[i][1] and productos[j][1]>r ):
           r = productos[j][1]
           max = productos[j][0]

  for n in index:
    for m in index:
        if(productos[m][1]<productos[n][1] and productos[m][1]<t ):
           t = productos[m][1]
           min = productos[m][0]
  
  med=w/len(productos)

  print(max,min,round(med,1),round(s,1))


index = list(range(1,len(productos)+1))



def Add(Codigo,Nombre,Precio,Stock):
    if(index.count(Codigo)>0):
        print("ERROR")
    else:
        index.append(Codigo)
        productos[Codigo]=[Nombre,Precio,Stock,0]
        Calc(productos)

def Act(Codigo,Nombre,Precio,Stock):
    if(index.count(Codigo)==0):
        print("ERROR")
    else:
        productos[Codigo]=[Nombre,Precio,Stock,0]
        Calc(productos)

def Del(Codigo,Nombre,Precio,Stock):
    if(index.count(Codigo)==0):
        print("ERROR")
    else:
        index.remove(Codigo)
        del(productos[Codigo])
        Calc(productos)

Accion = input()
a, b, c, d = input().split()

a=int(a)
c=int(c)
d=int(d)
if (Accion == "AGREGAR"):
    Add(a,b,c,d)
elif(Accion == "ACTUALIZAR"):
    Act(a,b,c,d)
elif(Accion == "BORRAR"):
    Del(a,b,c,d)


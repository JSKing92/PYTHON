Numero = int(input())

iterador =list(range(Numero))
Seleccionados = list()
for i in iterador:
    Medalla, Tiempo, Meses, Top, Edad = input().split()
    if (int(Medalla)>=3 and int(Tiempo)>=4 and int(Top)<=10 and int(Meses)<=24):
        Seleccionados.append(int(Edad))

Orden = list(range(len(Seleccionados)))

if len(Seleccionados)==0:
    print("NO DISPONIBLE")
else:
    for j in Orden:
        print(Seleccionados[j])



Distancia, Record, Tiempo =input().split()

float(Distancia)
float(Record)
float(Tiempo)

if int(Distancia) < 0 or int(Record) < 0 or int(Tiempo) < 0:
    print('MEDICION ERRONEA')
else:
   
    Velocidad = (int(Distancia)/1000)/(int(Tiempo)/3600)
    Variacion = abs((int(Record)-Velocidad)/int(Record))*100
    if  Velocidad > int(Record) and Variacion > 15:
        print('ENTREVISTA')
    else:
        if (Velocidad > int(Record) and Variacion < 15):
         print('NUEVO RECORD')
        else:
         print('VELOCIDAD NORMAL')

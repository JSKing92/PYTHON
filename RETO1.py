Salario, Horas, Bonificacion = input().split()
Salario = float(Salario)
Horas = int(Horas)
Bonificacion = int(Bonificacion)
Chora = Salario/192
Cextras = 1.25*Chora*Horas
Cbonif = 0.05*Salario*Bonificacion
Cdesc= Salario + Cextras + Cbonif
Desc = 0.085*Cdesc
Ctotal = Cdesc - Desc
print (round(Ctotal,1))



Salario = int(input('Salario base: '))
Horas = int(input('Horas extras: '))
Bonificacion = int(input('Bonificacion: '))
Chora = Salario/192
Cextras = 1.25*Chora*Horas
Cbonif = 0.05*Salario*Bonificacion
Cdesc= Salario + Cextras + Cbonif
Desc = 0.085*Cdesc
Ctotal = Cdesc - Desc
print ('Valor a pagar: ', round(Ctotal,2))



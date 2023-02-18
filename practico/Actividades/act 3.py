#1. Plazo fijo
#Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente de un banco y
#calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3% y
#que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.

dinero = int(input("ingrese la cantidad de dinero depositado: "))

porcentaje = dinero * (2.3/100)


dinero = dinero + porcentaje

dinero = dinero - 20

print("El saldo que tendra a vencer el plazo fijo sera de ", dinero)

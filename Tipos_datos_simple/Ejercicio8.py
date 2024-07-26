#Escribir un programa que pida al usuario dos números enteros y muestre 
# por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y 
# <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y 
# el resto de la división entera respectivamente.

m=int(input("Dame el primer numero entero: "))
n=int(input("Dame el segundo numero entero: "))

print("El cociente entre ",m, "y ",n," es ",(int((m/n)))," y el resto es ",(m%n))
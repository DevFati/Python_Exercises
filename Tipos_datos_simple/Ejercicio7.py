#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
# pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de
#  masa corporal calculado redondeado con dos decimales.

m=float(input("Dime tu peso en kg: "))

f=float(input("Dime tu estatura en metros: "))

g=m/(f ** 2)

input(round(g,2))
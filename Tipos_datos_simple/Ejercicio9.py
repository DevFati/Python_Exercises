#Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

m=float(input("Introduce cantidad a invertir: "))
n=float(input("Introduce el interes anual: "))
f=int(input("Introduce el numero de años: "))

print("El capital obtenido en la inversion es de: ",(round((m*(n/100+1)**f),2)))
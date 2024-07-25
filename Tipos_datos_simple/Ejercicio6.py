#Escribir un programa que lea un entero positivo, 
# , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
# . La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:

m=int(input("Dame un numero entero positivo: "))

if(m<=0):
    input("Numero introducido menor o igual a 0")
else:
    input((m*(m+1))/2)
    
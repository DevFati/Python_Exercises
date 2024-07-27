#Escribir un programa que pregunte el nombre del usuario en la consola y un número
#  entero e imprima por pantalla en líneas distintas el nombre del usuario tantas 
# veces como el número introducido.


m=input("Introduce tu nombre: ")
numero=int(input("Introduce un numero entero: "))
#1º Forma
n=0

while n!=numero:
    print(m)
    n=n+1

#2º Forma

print((m+"\n")*n)
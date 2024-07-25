#Escribir un programa que pregunte al usuario por el número de horas trabajadas 
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

m=float(input("Horas trabajadas: "))
n=float(input("Coste por hora: "))

print("La paga es de: ",(m*n)," euros.")

#Nota: No se pueden concatenar "+" un int con un string, para hacer eso hay que usar ","
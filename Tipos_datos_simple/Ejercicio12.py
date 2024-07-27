#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
# programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser 
# fresca y el coste final total.

barrasN=(int(input("Introduce la cantidad de barras que no son del dia: ")))

print("Las barras de pan cuestan normalmente 3.49 cada una, por lo que el total en ese caso seria de  ",round((3.49*barrasN),2)," euros.")
print("Al no ser freca se le hace un descuento del 60% por lo que tendria un descuento de ",round((barrasN*3.49*0.6),2)," euros")
print("El precio final seria de: ",round((barrasN*3.49*0.4),2))
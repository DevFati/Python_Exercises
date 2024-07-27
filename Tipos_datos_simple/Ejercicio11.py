#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
# depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
# y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
#  cantidad a dos decimales.

dinero=float(input("Introduce cantidad de dinero depositada en la cuenta: "))
interes1=1.04*dinero
print("Ahorros despues de 1 año: ",round(interes1,2), " euros")
interes2=interes1*1.04
print("Ahorros despues de 2 año: ",round(interes2,2), " euros")
interes3=interes2*1.04
print("Ahorros despues de 3 año: ",round(interes3,2), " euros")


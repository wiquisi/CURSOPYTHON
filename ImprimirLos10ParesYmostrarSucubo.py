#Decoracion del nombre del Algoritmo
print("-------------------------")
print("IMPRIMIR LOS 10 PRIMEROS PARES Y SUS CUBOS")
#entradas
#inicializar
i=2
#proceso
while i<=20:
    if i%2==0:
        p=i**3
        print("El cubo de",i "es", p)
    i=i+1

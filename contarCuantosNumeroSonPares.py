print("--------------------------------")
print("Contar cuantos numeros son pares")
print("--------------------------------")

#INICIALIZAMOS
i=1
c=0
numEntradas=10

#Procesos
print("Ingrese",numEntradas,"Numeros:")
while i<=numEntradas:
    n=int(input("ingrese numero:"))
    if n%2==0:
        c=c+1
    i=i+1
#Salida
print("\nSALIDA:")
print("------------------------")
print("En",numEntradas,"nùmeros enteros hay",c,"numeros pares")
from funciontuplas2ejercicio import *
#1
numeros=[]
nro=int(input("Numero:"))
while nro!=0:
    numeros.append(nro)
    nro=int(input("numero:"))
#2
eliminar =int(input("numero a eliminar: "))
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Este numero no està entre los ingresados")
#3
print("Sumatoria de los numeros:", sumatoria(numeros))

#4
limite= int(input("filtrar numeros menores a:"))
for n in numerosMenores(numeros,limite):
    print(n)

#5
print ("Frecuencias:")
for tupla in Frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces")

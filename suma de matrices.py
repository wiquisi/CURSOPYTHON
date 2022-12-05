print("---------------------------------")
print("...... SUMA DE MATRICES..........")
print("---------------------------------")
#INICIALIZAR
A=[]
B=[]
C=[]

#Entradas
print("ingrese dimension de la matriz, maximo 100")
S=int(input("Numeros de Filas:"))
R=int(input("Numero columnas:"))
#Proceso
for i in range(S):
    A.append([])#agregamos una i fila vacia en A
    B.append([])  # agregamos una i fila vacia en B
    C.append([])  # agregamos una i fila vacia en C
    for j in range(R):
        A[i].append(int(input("A{}{}:".format(i+1,j+1))))
        B[i].append(int(input("B{}{}:".format(i+1,j+1))))
        C[i].append(A[i][j]+B[i][j])
#Salida
print("\nSalida")
print("------------------------------------")
print(A)
print(B)
print(C)

A=[20,35,10,40,4,5,6,7,30]
mayor=A[0];
menor=A[0];
for x in range (0,9):
      if (A[x]>mayor):
        mayor=A[x];
      if(A[x]<menor):
       menor=A[x];
print("El mayor valor del vector es de : " + str(mayor) + "\n");
print("El menor valor del vector es de : " + str(menor));
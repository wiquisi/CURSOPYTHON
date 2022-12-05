A=[50,75,46,22,80,65,8]
mayor=A[0];
menor=A[0];
for x in range (0,7):
      if (A[x]>mayor):
        mayor=A[x];
      if(A[x]<menor):
       menor=A[x];
print("El mayor valor del vector es de : " + str(mayor) + "\n");
print("El menor valor del vector es de : " + str(menor));
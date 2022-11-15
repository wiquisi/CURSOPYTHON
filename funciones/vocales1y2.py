vocales1=['a','e']
vocales2=['i','o','u']
vocales1.extend(vocales2)
#actualizamos la letra o minuscula por dos 00
vocales1[3]='00'
#para eliminar la letra u del array
vocales1.remove('u')
print(vocales1)

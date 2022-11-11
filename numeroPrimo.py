#numero=int(input("ingrese el numero"))
#for n in range(2,numero):
#    if numero%n == 0:
#        print(numero,"el numero ingresado NO es primo")
#        continue
#    else:
#        print(numero,"el numero ingresado es primo")
a=3473
def es_primo(num):
    contador = 0
    for i in range(1, num+1):
        if num%i == 0:
            contador += 1

    if contador == 2:
        return True
    else:
        return False

    print(es_primo(a))
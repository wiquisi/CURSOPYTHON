#escriba una funcion que
# #acepte una lista y genere
# otra lista eliminando los numeros duplicados
#entrada[1,1,2,2,3,4,4,5,6,6]
#salida=[1,2,3,4,5,6]
numerosdup = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]
def delduplicate(numerosdup):
    numerosdup=[1,1,2,2,3,4,4,5,6,6]
    uniconumero=[]
    for numero in numerosdup:
        if numero not in uniconumero:
            uniconumero.append(numero)
            return uniconumero
        print(delduplicate(uniconumero)
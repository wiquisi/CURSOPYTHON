#Escribir una funcion que almacene en una lista los precios
# , 50,75,46,22,80,65,8
# y muestre por pantallas el menor y mayor precio

precios=(50,75,46,22,80,65,8)
def  num_min():
    return min(precios)
print("El precio màs barato es de:",num_min())
def num_max():
    return max(precios)
print("El percio màs carito del producto es:",num_max())


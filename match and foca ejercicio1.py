##tendremos una variable con el mensaje hola mundo
##pedir al usuario que  ingrese un texto
##si el texto ingresado es hola
##mostraras el mensaje completo
##si el texto ingreso es como estas
##extraeras el mensaje del mensaje la palabra hola
##si el texto ingresad es saludos
##extraeras del mensaje la palabra mundo
##si se ingresa otro texto
##mostrar por defecto  el mensaje error

mensaje="hola mundo"
texto=input("ingrese un texto")
match texto:
    case "hola":
        print(mensaje[:])
    case "como estas":
        print (mensaje[:4])
    case "saludos":
        print(mensaje[5:])
    case  _:
        print("error")

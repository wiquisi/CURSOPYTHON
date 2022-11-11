##OPERACION CON FUNCION
##UTILIZAR LA PALABRARESERVADA DEF
##ASIGNAMOS UN NOMBRE DESCRIPTIVO  A LA FUNCION
##SIEMPRE TIENE QUE RECIBIR PARAMETROS
##()-- NO RECIVE PARAMETROS
##(NOMBRE)--- QUE LA FUNCION ESTÈ RECIBIENDO UN PARAMETRO
##(EDAD,NOMBRE)
##SIEMPRE LA FUNCION TIENE QUE RETORNAR UN TIPO DE DATO

## funcion saludo
def saludo():
    respuesta="hola como estas"
    return respuesta

##como uso la funcion
##estoy llamando a la funcion interna de pytho con funcio
arrayamigos= ['ronals', 'claudio,"diego","jose","mozart","lilia" ]
              for amigo in range (0,len(arrayamigos)):
                  print(saludo(arrayamigos[amigo]))
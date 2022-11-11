def operaciones(num1,num2,operador):
    if operador=='suma':
        total=num1+num2
    if operador=='resta':
        total=num1-num2
    if operador=='por':
        total=num1*num2
    if operador=='entre':
        total=num1/num2
    return total
operacion= "resta"
match operacion:
    case "suma":
        print("realizaré una suma")
    case "resta":
         print("realizare una resta")
    case "multiplicacion":
           print("realizare una multiplicacion")
    case _:
               print("no hay operaciones")
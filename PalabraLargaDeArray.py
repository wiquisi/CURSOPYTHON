def palabra_larga(palabras):
    palabra_longitud=[]

    for p in palabras:
        palabra_longitud.append((len(p),p))
    print(palabra_longitud)
    palabra_longitud.sort()
    print(palabra_longitud)
    return palabra_longitud[-1][1]
palabras=["java Script","pyhton","c++","PHP"]
print(palabra_larga(palabras))
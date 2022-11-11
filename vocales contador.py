sentence=input("enter sentence:")
vocales=["a","e","i","o","u"]
def countVocal(oracion,vocal):
    contador=0
    for word in oracion :
        if word in vocal:
            contador+=1
    return contador
print(countVocal(sentence,vocales))
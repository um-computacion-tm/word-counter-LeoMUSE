def countWords(frase):

    palabras = {}

    palabrasLista = frase.lower().split()

    for palabra in palabrasLista:

        if palabra in palabras:
            palabras[palabra] += 1
    
        else:
            palabras[palabra] = 1

    resultado = palabras
    return resultado

if __name__ == "__main__":
    pass
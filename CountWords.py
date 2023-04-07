def countWords(frase):

    palabras = {}

    palabras_lista = frase.lower().split()

    for palabra in palabras_lista:

        if palabra in palabras:
            palabras[palabra] += 1
    
        else:
            palabras[palabra] = 1

    resultado = palabras
    return resultado

if __name__ == "__main__":
    pass
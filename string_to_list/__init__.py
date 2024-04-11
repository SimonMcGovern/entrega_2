def string_multiline_transformer(str1):
    """
    Esta funcion recibe un string multilinea pasado por parametro y lo transforma a una lista uniforme
    """
    characters = [',', "'"]

    for character in characters:
        str1 = str1.replace(character, "")

    str1 = " ".join(str1.splitlines())

    str1 = str1.split(" ")

    str1 = list(filter(lambda word: word != "", str1))
    return str1
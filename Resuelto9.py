def omitir_vocales(cadena):
    # Definir las vocales en minúsculas y en mayúsculas
    vocales = 'aeiouAEIOU'
    # Inicializar una cadena vacía para almacenar el resultado
    resultado = ''
    # Iterar sobre cada carácter en la cadena de entrada
    for char in cadena:
        # Si el carácter no es una vocal, añadirlo al resultado
        if char not in vocales:
            resultado += char
    return resultado

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")
# Llamar a la función omitir_vocales y mostrar el resultado
print("Texto con las vocales omitidas:", omitir_vocales(cadena))

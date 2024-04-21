def contar_digito_en_numero(numero, digito):
    """
    Esta función recibe un número y un dígito, y retorna la cantidad de veces que el dígito aparece en el número.

    Args:
    numero (int): El número en el que se buscará el dígito.
    digito (int): El dígito cuya cantidad de apariciones se quiere contar.

    Returns:
    int: La cantidad de veces que el dígito aparece en el número.
    """
    # Convertir el número y el dígito a cadena para poder utilizar el método count
    str_numero = str(numero)
    str_digito = str(digito)

    # Utilizar el método count para contar las apariciones del dígito en el número
    cantidad = str_numero.count(str_digito)

    # Devolver el resultado
    return cantidad

# Ejemplo de uso de la función
numero = 15789000
digito = 0
resultado = contar_digito_en_numero(numero, digito)
print(f"Cantidad de veces {digito} en el número {numero}: {resultado}")

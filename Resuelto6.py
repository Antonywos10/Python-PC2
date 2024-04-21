def fibonacci_hasta_maximo(maximo):
    """
    Esta función genera la serie de Fibonacci hasta un número máximo dado.
    
    Args:
    maximo (int): El límite superior para los valores de la serie de Fibonacci.
    
    Returns:
    list: Lista conteniendo la serie de Fibonacci hasta el máximo especificado.
    """
    # Inicializar los dos primeros términos
    a, b = 0, 1
    # Lista para almacenar la serie de Fibonacci
    serie_fibonacci = []
    
    # Continuar hasta que el próximo valor sea mayor que el máximo
    while a <= maximo:
        serie_fibonacci.append(a)
        # Calcular el siguiente término de la serie
        a, b = b, a + b
    
    return serie_fibonacci

# Llamando a la función para obtener la serie de Fibonacci hasta 50
fibonacci_resultado = fibonacci_hasta_maximo(50)
print("Serie de Fibonacci entre 0 y 50:")
print(fibonacci_resultado)

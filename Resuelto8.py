def factorial(numero):
    # El factorial de 0 es 1
    if numero == 0:
        return 1
    # Inicializar el resultado del factorial como 1
    resultado = 1
    # Calcular el factorial multiplicando el número por todos los enteros positivos menores que él
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")

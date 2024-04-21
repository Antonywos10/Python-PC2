# Lista para almacenar los números que cumplen las condiciones
numeros_validos = []

# Iterar sobre el rango de números de 1500 a 2700 (ambos incluidos)
for numero in range(1500, 2701):
    # Verificar si el número es divisible por 7 y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        numeros_validos.append(numero)

# Imprimir los números encontrados
print("Números que son divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")
print(numeros_validos)

# Número máximo de estrellas en la línea más larga
num_max_estrellas = 5

# Parte creciente del patrón
for i in range(1, num_max_estrellas + 1):
    # Imprimir 'i' estrellas en una línea
    print('* ' * i)

# Parte decreciente del patrón
for i in range(num_max_estrellas - 1, 0, -1):
    # Imprimir 'i' estrellas en una línea
    print('* ' * i)

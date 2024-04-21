# Lista para almacenar los números ingresados
numeros = []

# Contadores para números pares e impares
cont_pares = 0
cont_impares = 0

# Bucle para pedir números al usuario
while True:
    # Preguntar al usuario si desea ingresar un número
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    
    # Procesar la respuesta del usuario
    if respuesta.upper() == "SI":
        # Solicitar al usuario que ingrese un número
        numero = int(input("Ingrese el número: "))
        
        # Añadir el número a la lista de números
        numeros.append(numero)
        
        # Determinar si el número es par o impar y actualizar contadores
        if numero % 2 == 0:
            cont_pares += 1
        else:
            cont_impares += 1
    elif respuesta.upper() == "NO":
        # Salir del bucle
        break
    else:
        print("Respuesta no válida. Por favor ingrese SI o NO.")

# Mostrar los resultados
print("Números ingresados:", numeros)
print("Cantidad de números pares:", cont_pares)
print("Cantidad de números impares:", cont_impares)


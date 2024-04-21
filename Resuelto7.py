def es_primo(numero):
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False
    # Verificar si el número es divisible por algún número menor que él mismo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso
numero = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

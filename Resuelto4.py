def ingresar_datos():
    # Lista para almacenar los datos de los alumnos
    alumnos = []

    # Leer la cantidad de alumnos a ingresar
    n = int(input("Ingrese la cantidad de alumnos: "))

    # Bucle para ingresar los datos de cada alumno
    for i in range(n):
        # Leer el nombre del alumno
        nombre = input(f"Nombre del alumno {i + 1}: ")

        # Leer las tres calificaciones
        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la calificación {j + 1} de {nombre}: "))
            notas.append(nota)

        # Crear un diccionario con los datos del alumno y añadirlo a la lista
        alumno = {
            "Alumno": nombre,
            "Notas": notas
        }
        alumnos.append(alumno)

    # Devolver la lista de alumnos
    return alumnos

def mostrar_alumnos(alumnos):
    # Mostrar los datos de cada alumno
    print("\nListado de Alumnos y sus Calificaciones:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Programa principal
alumnos = ingresar_datos()
mostrar_alumnos(alumnos)

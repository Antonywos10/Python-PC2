import re

def convertir_fecha(fecha):
    # Expresión regular para buscar un patrón de fecha en el formato deseado
    patron_fecha = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})|(\w+) (\d{1,2}), (\d{4})')
    
    # Buscar el patrón de fecha en la entrada del usuario
    match = patron_fecha.match(fecha)
    
    if match:
        # Si la fecha está en el formato mes-día-año
        if match.group(1):
            mes = int(match.group(1))
            dia = int(match.group(2))
            año = int(match.group(3))
        # Si la fecha está en el formato "Mes día, año"
        elif match.group(4):
            nombre_mes = match.group(4)
            dia = int(match.group(5))
            año = int(match.group(6))
            # Diccionario que mapea el nombre del mes a su número correspondiente
            meses = {
                "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
                "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
            }
            mes = meses[nombre_mes]
        
        # Formatear la fecha en el formato AAAA-MM-DD
        fecha_formateada = f"{año}-{mes:02d}-{dia:02d}"
        return fecha_formateada
    else:
        return "Formato de fecha no válido"

# Solicitar al usuario que ingrese una fecha
fecha_usuario = input("Ingrese una fecha (en formato mes-día-año o Mes día, año): ")

# Llamar a la función convertir_fecha y mostrar el resultado
print("Fecha en formato AAAA-MM-DD:", convertir_fecha(fecha_usuario))

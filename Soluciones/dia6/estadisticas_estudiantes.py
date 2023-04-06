# Leer de los archivos
# Esta funcion abre el archivo con los estudiantes y regresa una list de strings
def leer_informacion_estudiantes():
    nombre_archivo_datos = 'estudiantes.txt'
    lista_estudiantes = []
    # Open file
    with open(nombre_archivo_datos) as file:
        lineas = file.readlines()
        for linea in lineas:
            atributos_estudiante = linea.split(', ')
            # Eliminar character de nueva linea
            atributos_estudiante[-1] = atributos_estudiante[-1][:-1]
            lista_estudiantes.append(atributos_estudiante)
    return lista_estudiantes

class Estudiante:
    def __init__(self, id, nombre, apellido, correo, calificaciones):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.calificaciones = calificaciones

    def promedio(self):
        # Completa esta funcion para que retorne el promedio de un estudiante
        return sum(self.calificaciones) / len(self.calificaciones)

    def __lt__(self, other):
        return self.promedio() < other.promedio()

    def aprueba(self):
        return self.promedio() > 7

    def __str__(self):
        aprueba_str = 'Aprueba' if self.aprueba() else 'No aprueba'
        return str(self.id).ljust(5) + self.nombre.ljust(15) + self.apellido.ljust(15) \
                + self.correo.ljust(30) + "{:10.4f}".format(self.promedio()).ljust(15) + aprueba_str.ljust(15)

datos_estudiantes = leer_informacion_estudiantes()
estudiantes = []
for datos_estudiante in datos_estudiantes:
    id = datos_estudiante[0]
    apellido = datos_estudiante[1]
    nombre = datos_estudiante[2]
    correo = datos_estudiante[3]
    calificaciones = datos_estudiante[4::]
    calificaciones = [float(calificacion) for calificacion in calificaciones]
    nuevo_estudiante = Estudiante(id, nombre, apellido, correo, calificaciones)
    estudiantes.append(nuevo_estudiante)


print('*' * 100)
print('ID'.ljust(5) + 'Nombre'.ljust(15) + 'Apellido'.ljust(15) \
        + 'Correo electronico'.ljust(30) + 'Promedio'.ljust(15) + 'Resultado'.ljust(15))
print('*' * 100)

estudiantes_ordenados = sorted(estudiantes, reverse=True)
for estudiante in estudiantes_ordenados:
    print(estudiante)

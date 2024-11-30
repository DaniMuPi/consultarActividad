from cargarActividad import cargarActividad

def consultarActividad(archivoActividad):
    actividad_dict = cargarActividad(archivoActividad)
    return len(actividad_dict)


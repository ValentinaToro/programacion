
#uso de diccionarios, creando una base de datos usando listas o tuplas como elementos de esta lista.
#Esta base de datos deberá representar una lista de curso similar a la vista en clases, 
#que incluya 4 alumnos con sus nombres y las notas en dos cursos (‘programacion’ y ‘fisica’). 
# Deberán imprimir los resultados para uno de estos alumnos.
print ("Alumnos empleados y sus notas")
Alvaro = (5.3 , 4.5)
print (Alvaro)
Constanza = (4.0 , 4.3)
print (Constanza)
Isidora = (4.1 , 5.5)
print (Isidora)
Ignacio = (5.1 , 4.7)
print (Ignacio)
#hago el diccionario con estos datos.
diccionario = [
    { 'nombre': 'Alvaro', 'programacion': '5.3', 'fisica': '4.5'},
    {'nombre': 'Constanza', 'programacion': '4.0', 'fisica': '4.3'},
    {'nombre': 'Isidora', 'programacion': '4.1', 'fisica': '5.5'},
    {'nombre': 'Ignacio', 'programacion': '5.1', 'fisica': '4.7'}
]
#para corroborar si es un diccionario, reviso el tipo:
#para recorrer un diccionario se requiere un ciclo o bucle
print('  Curso  ')
for d in diccionario:
    print(f"Nombre: {d['nombre']} | Nota Programacion: {d['programacion']} | Nota Fisica: {d['fisica']}")

print('Ahora imprimiré el tipo para corroborar y la información de un alumno.')
print (type (diccionario))
print (diccionario[2]['nombre'])
print (diccionario[2]['programacion'])
print (diccionario[2]['fisica'])
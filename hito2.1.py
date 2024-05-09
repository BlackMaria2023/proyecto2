

from django.db import connection
import os

consulta_sql = """
    SELECT c.nombre AS comuna, i.nombre AS nombre_inmueble, i.descripcion
    FROM app_inmueble i
    JOIN app_comuna c ON i.comuna_id = c.id
    WHERE i.disponible = TRUE
"""

with connection.cursor() as cursor:
    cursor.execute(consulta_sql)
    resultados = cursor.fetchall()

resultados_file = 'listado_inmuebles_comuna.txt'
with open(resultados_file, "w") as file:
    for row in resultados:
        comuna, nombre_inmueble, descripcion = row
        file.write(f"Comuna: {comuna}\n")
        file.write(f"Nombre del inmueble: {nombre_inmueble}\n")
        file.write(f"Descripcion: {descripcion}\n")
        file.write("\n")
        
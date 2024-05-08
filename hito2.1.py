import os
import django
from django.db import connection

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HogarDeEnsuenio.settings')
django.setup()

# Obtener el nombre de la región que quieres consultar
nombre_region = "Tarapacá"

# Consulta SQL para obtener los inmuebles por región
consulta_sql = """
    SELECT i.nombre, i.descripcion
    FROM app_inmueble AS i
    INNER JOIN app_comuna AS c ON i.comuna_id = c.id
    INNER JOIN app_region AS r ON c.region_id = r.id
    WHERE r.nombre = %s;
"""

# Ejecutar la consulta SQL
with connection.cursor() as cursor:
    cursor.execute(consulta_sql, [nombre_region])
    resultados = cursor.fetchall()

# Guardar los resultados en un archivo de texto
with open('inmuebles_por_region.txt', 'a') as archivo:
    for nombre, descripcion in resultados:
        archivo.write(f"Nombre: {nombre}\nDescripción: {descripcion}\n\n")

        
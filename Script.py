import requests  # Importar la biblioteca requests para hacer solicitudes HTTP
import csv  # Importar la biblioteca csv para trabajar con archivos CSV
import time  # Importar la biblioteca time para manejar intervalos de tiempo

while True:  # Bucle infinito para ejecutar la tarea repetidamente
    try:
        response = requests.get('http://localhost:5000/data')  # Hacer una solicitud GET a la API
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        data = response.json()  # Obtener los datos en formato JSON

        with open('data.csv', mode='w', newline='') as file:  # Abrir un archivo CSV en modo escritura
            writer = csv.writer(file)  # Crear un escritor de CSV
            writer.writerow(['Column1', 'Column2'])  # Escribir los encabezados de las columnas
            for row in data:  # Iterar sobre los datos obtenidos
                writer.writerow(row)  # Escribir cada fila en el archivo CSV

        print("Datos guardados exitosamente.")
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud a la API: {e}")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

    time.sleep(3600)  # Esperar una hora (3600 segundos) antes de la siguiente ejecución
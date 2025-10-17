import csv
import os

# Nombre del archivo que queremos leer
nombre_archivo = 'paises.csv'

print(f"--- Iniciando prueba de lectura para '{nombre_archivo}' ---")

# Verificamos si el archivo existe en la carpeta actual
if not os.path.exists(nombre_archivo):
    print(f"\nERROR FATAL: No se encuentra el archivo '{nombre_archivo}' en la misma carpeta que este script.")
    print(f"Asegúrate de que 'test.py' y '{nombre_archivo}' estén juntos.")
else:
    print("\n¡Éxito! El archivo fue encontrado en la carpeta.")
    
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            print("El archivo se abrió correctamente (codificación utf-8).")
            
            # Usamos el delimitador de punto y coma
            lector_csv = csv.DictReader(archivo, delimiter=';')
            
            # Leemos la primera fila para verificar las columnas
            primera_fila = next(lector_csv)
            columnas = list(primera_fila.keys())
            
            print(f"\nLas columnas detectadas son: {columnas}")
            
            # Verificamos si las columnas necesarias están presentes
            columnas_necesarias = ['nombre', 'poblacion', 'superficie', 'continente']
            todo_ok = True
            for col in columnas_necesarias:
                if col not in columnas:
                    print(f"ERROR: Falta la columna esperada '{col}' en el archivo CSV.")
                    todo_ok = False
            
            if todo_ok:
                print("\n¡Prueba superada! Todas las columnas necesarias fueron encontradas.")
                print("El archivo CSV es legible y tiene el formato correcto.")

    except Exception as e:
        print(f"\nERROR INESPERADO: Ocurrió un problema al procesar el archivo: {e}")

print("\n--- Fin de la prueba ---")
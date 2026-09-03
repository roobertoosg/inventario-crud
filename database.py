import os
import psycopg2
import logging
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env a la memoria
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# 2. Función para conectarnos a la base de datos
def probar_conexion():
    try:
        # Intentamos abrir la conexión usando los datos seguros
        conexion = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        
        logging.info("Conexión a PostgreSQL exitosa.")
        
        # Cerramos la conexión porque solo queríamos probar
        conexion.close()
        logging.info("Conexión cerrada correctamente.")

    except Exception as error:
        logging.error(f"Error al conectar con la base de datos: {error}")

# 3. Ejecutamos la función solo para probar
probar_conexion()
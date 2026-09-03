import logging
from database import engine, Base
# Importamos el modelo para que la 'Base' lo detecte antes de crear las tablas
from models import Producto 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def iniciar_db():
    try:
        logging.info("Iniciando la creacion de tablas en la base de datos...")
        # Aquí usamos el motor y la base que importamos
        Base.metadata.create_all(bind=engine)
        logging.info("Tablas creadas exitosamente en la base de datos.")
    except Exception as e:
        logging.error(f"Error al iniciar la base de datos: {e}")


if __name__ == "__main__":
    iniciar_db()
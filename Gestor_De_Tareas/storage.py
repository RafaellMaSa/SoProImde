import json

# Ruta por defecto para el archivo JSON
DEFAULT_FILE = 'tasks.json'

def save_tasks(tasks, file_path=DEFAULT_FILE):

    try:
        with open(file_path, 'w') as f:
            json.dump(tasks, f, indent=4)
        print(f"Tareas guardadas exitosamente en {file_path}.")
    except Exception as e:
        print(f"Error al guardar tareas: {e}")

def load_tasks(file_path=DEFAULT_FILE):
    """
    Cargar las tareas desde un archivo JSON.
    
    :param file_path: Ruta del archivo de donde se cargarán las tareas.
    :return: Lista de tareas cargada desde el archivo (o una lista vacía si no existe).
    """
    try:
        with open(file_path, 'r') as f:
            tasks = json.load(f)
        print(f"Tareas cargadas exitosamente desde {file_path}.")
        return tasks
    except FileNotFoundError:
        print(f"Archivo {file_path} no encontrado. Se creará uno nuevo.")
        return []  # Si no hay archivo, devuelve una lista vacía
    except json.JSONDecodeError:
        print(f"Error al leer el archivo {file_path}. Formato inválido.")
        return []  # Devuelve una lista vacía si el archivo tiene un formato incorrecto
    except Exception as e:
        print(f"Error al cargar tareas: {e}")
        return []

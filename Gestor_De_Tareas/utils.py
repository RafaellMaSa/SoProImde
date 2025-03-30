from datetime import datetime

def validate_integer_input(value):
    

    try:
        return int(value)
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
        return None

def validate_date_format(date_string, format="%Y-%m-%d"):
 
    try:
        return datetime.strptime(date_string, format)
    except ValueError:
        print(f"Error: La fecha '{date_string}' no tiene el formato correcto ({format}).")
        return None

def format_date(date_obj):
  
    if date_obj:
        return date_obj.strftime("%Y-%m-%d")
    return "No especificada"

def generate_unique_id(tasks):
 
    if tasks:
        max_id = max(task['id'] for task in tasks)
        return max_id + 1
    return 1 

def print_massage(massage, massage_type = "info"): 
    if massage_type == "info":
        print (f"[INFO] {massage}")

    elif massage_type == "error":
        print (f"[ERROR] {massage}")
    
    elif massage_type =="success":
        print(f"[SUCCESS]{massage}")

    else: 
        print(massage)
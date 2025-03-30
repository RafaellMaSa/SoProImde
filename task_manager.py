import json
from tasks i
def display_menu():
    print("\nGestor de Tareas")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input ("Elige una opcion (1-5)")

        if choice == '1': 
            title = input('Introduce el titulo de la tarea:')
            description = input('Introduce la descripcion de la tarea: ')
            due_date = input('Introduce la fecha de vencimiento : ')
            tasks = add_task(tasks,title, descripton, due_date)
            save_tasks(tasks)
        elif choice == '2':
            view_task(tasks)

        elif choice == '3':
            task_id = int(input("Introduce el ID de la terea a carca como completada"))
            tasks = mark_task(tasks, task_id)
            save_tasks(tasks)
             
        elif choice == '4': 
            task_id = int(input("Introduce el ID de la tarea a eliminar "))
            tasks = remove_task(tasks, task_id)
            save_tasks(tasks)

        elif choice == '5': 
            print ("Saliendo del programa.")

        else:
            print ("Opcion no valida. Por favor, elija una opcion del 1 al 5.")

    if __name__== "__main__":
        main()
 
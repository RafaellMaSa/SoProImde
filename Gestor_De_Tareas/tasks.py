def add_task(tasks, title, descripton, due_date= None):
    task_id = len(tasks) + 1
    new_task = {
        'id' : task_id,
        'title' : title,
        'description' : descripton,
        'due_date' : due_date,
        'completed' : False
    }
    tasks.append(new_task)
    return tasks 
def remove_task(tasks, task_id):
    task_remove = next((task for task in tasks if task ['id']==task_id),None)
    if task_remove:
        tasks.remove(task_remove)
        return tasks
    else:
        print(f'Tarea con ID {task_id} no encontrada.')
        return tasks
def mark_task(tasks, task_id):
    task_to_mark = next((task for task in tasks if task['id']== task_id), None)
    if task_to_mark:
        task_to_mark['completed'] = True
        return tasks
    else: 
        print(f'Tarea con ID {task_id} no encontrada.')
        return tasks
def view_task(tasks):
    if not tasks:
        print('No hay tareas registradas.')
    for task in tasks:
        status = 'Completada' if task['completed'] else 'Pendiente'
        print (f"ID: {task['id'] } | Titulo: {task['title']} | Estado: {status} | Fecha de vencimiento: {task['due_date']}")

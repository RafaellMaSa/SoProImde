import tkinter as tk
from tkinter import messagebox
from storage import save_tasks, load_tasks
from tasks import add_task, remove_task, mark_task
from utils import validate_date_format, format_date, generate_unique_id


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        
        # Cargar tareas desde JSON
        self.tasks = load_tasks()

        # Crear componentes
        self.create_widgets()

    def create_widgets(self):
        # Listbox para mostrar tareas
        self.task_list = tk.Listbox(self.root, width=50, height=15)
        self.task_list.pack(pady=10)
        self.update_task_list()

        # Formulario para agregar tareas
        self.title_label = tk.Label(self.root, text="Título:")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.root, width=40)
        self.title_entry.pack()

        self.desc_label = tk.Label(self.root, text="Descripción:")
        self.desc_label.pack()
        self.desc_entry = tk.Entry(self.root, width=40)
        self.desc_entry.pack()

        self.date_label = tk.Label(self.root, text="Fecha (YYYY-MM-DD, opcional):")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root, width=40)
        self.date_entry.pack()

        # Botones
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task_gui)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task_gui)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task_gui)
        self.delete_button.pack(pady=5)

    def update_task_list(self):
        """Actualizar la lista de tareas en el Listbox."""
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "✔" if task['completed'] else "✘"
            self.task_list.insert(tk.END, f"[{status}] {task['id']}: {task['title']} (Vence: {task['due_date']})")

    def add_task_gui(self):
        """Agregar una nueva tarea desde la GUI."""
        title = self.title_entry.get()
        description = self.desc_entry.get()
        due_date_input = self.date_entry.get()
        due_date = validate_date_format(due_date_input) if due_date_input else None

        if title and description:
            task_id = generate_unique_id(self.tasks)
            self.tasks = add_task(self.tasks, title, description, format_date(due_date))
            save_tasks(self.tasks)
            self.update_task_list()
            self.clear_form()
            messagebox.showinfo("Éxito", "Tarea añadida correctamente.")
        else:
            messagebox.showerror("Error", "El título y la descripción son obligatorios.")

    def complete_task_gui(self):
        """Marcar una tarea como completada desde la GUI."""
        try:
            selected_index = self.task_list.curselection()[0]
            task_id = self.tasks[selected_index]['id']
            self.tasks = mark_task(self.tasks, task_id)
            save_tasks(self.tasks)
            self.update_task_list()
            messagebox.showinfo("Éxito", "Tarea marcada como completada.")
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task_gui(self):
        """Eliminar una tarea desde la GUI."""
        try:
            selected_index = self.task_list.curselection()[0]
            task_id = self.tasks[selected_index]['id']
            self.tasks = remove_task(self.tasks, task_id)
            save_tasks(self.tasks)
            self.update_task_list()
            messagebox.showinfo("Éxito", "Tarea eliminada correctamente.")
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona una tarea para eliminar.")

    def clear_form(self):
        """Limpiar los campos del formulario."""
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
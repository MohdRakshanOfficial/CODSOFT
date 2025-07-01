import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "todo_data.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("400x500")
        self.tasks = load_tasks()

        # Entry for new task
        self.task_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.task_var, font=("Arial", 14))
        self.entry.pack(pady=10, padx=10, fill=tk.X)

        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Listbox to show tasks
        self.task_listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Buttons
        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.done_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_into_listbox()

    def add_task(self):
        title = self.task_var.get().strip()
        if not title:
            messagebox.showwarning("Warning", "Task cannot be empty.")
            return
        self.tasks.append({"title": title, "done": False})
        self.task_var.set("")
        self.load_into_listbox()
        save_tasks(self.tasks)

    def load_into_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["done"] else "❌"
            self.task_listbox.insert(tk.END, f"{status} {task['title']}")

    def mark_done(self):
        index = self.task_listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Select a task to mark as done.")
            return
        idx = index[0]
        self.tasks[idx]["done"] = True
        self.load_into_listbox()
        save_tasks(self.tasks)

    def delete_task(self):
        index = self.task_listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Select a task to delete.")
            return
        idx = index[0]
        task_title = self.tasks[idx]["title"]
        del self.tasks[idx]
        self.load_into_listbox()
        save_tasks(self.tasks)
        messagebox.showinfo("Deleted", f"Deleted task: {task_title}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


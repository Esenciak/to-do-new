from tkinter import *

def ladowanie():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(entry, listbox, tasks):
    new_task = entry.get()
    if new_task:
        tasks.append(new_task)
        listbox.insert(END, f"{len(tasks)}. {new_task}")
        save_tasks(tasks)
        entry.delete(0, END)

def delete_task(listbox, tasks):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del tasks[index]
        listbox.delete(selected_index)
        save_tasks(tasks)

def mark_done(listbox, tasks):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = tasks[index]
        if not task.startswith("[Done] "):
            tasks[index] = f"[Done] {task}"
            listbox.delete(selected_index)
            listbox.insert(END, tasks[index])
            save_tasks(tasks)

def main():
    root = Tk()
    root.title('ToDo List')
    root.geometry('400x400')

    tasks = ladowanie()

    listbox = Listbox(root, selectbackground='Gold', font=('Helvetica', 12), height=15, width=40)
    listbox.pack(pady=10)

    for i, task in enumerate(tasks, start=1):
        listbox.insert(END, f"{i}. {task}")

    entry = Entry(root, width=40)
    entry.pack(pady=10)

    add_button = Button(root, text='Add Task', command=lambda: add_task(entry, listbox, tasks))
    add_button.pack(side=LEFT, padx=10)

    delete_button = Button(root, text='Delete Task', command=lambda: delete_task(listbox, tasks))
    delete_button.pack(side=LEFT, padx=10)

    done_button = Button(root, text='Mark Done', command=lambda: mark_done(listbox, tasks))
    done_button.pack(side=LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()

from tkinter import *

def Zaladuj():
    try:
        with open('tasks.txt', 'r') as file:
            zadanie = [line.strip() for line in file.readlines()]
        return zadanie
    except FileNotFoundError:
        return []

def zapisz(zadanie):
    with open('tasks.txt', 'w') as file:
        for task in zadanie:
            file.write(f"{zadanie}\n")

def dodaj(entry, listbox, zadanie):
    new_task = entry.get()
    if new_task:
        zadanie.append(new_task)
        listbox.insert(END, f"{len(zadanie)}. {new_task}")
        zapisz(zadanie)
        entry.delete(0, END)

def usun(listbox, zadanie):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del zadanie[index]
        listbox.delete(selected_index)
        zapisz(zadanie)

def zaznacz(listbox, zadanie):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = zadanie[index]
        if not task.startswith("[Done] "):
            zadanie[index] = f"[Done] {task}"
            listbox.delete(selected_index)
            listbox.insert(END, zadanie[index])
            zapisz(zadanie)

def main():
    root = Tk()
    root.title('ToDo List')
    root.geometry('400x400')

    zadanie = Zaladuj()

    listbox = Listbox(root, selectbackground='Gold', font=('Helvetica', 12), height=15, width=40)
    listbox.pack(pady=10)

    for i, task in enumerate(zadanie, start=1):
        listbox.insert(END, f"{i}. {task}")

    entry = Entry(root, width=40)
    entry.pack(pady=10)

    add_button = Button(root, text='Add Task', command=lambda: dodaj(entry, listbox, zadanie))
    add_button.pack(side=LEFT, padx=10)

    delete_button = Button(root, text='Delete Task', command=lambda: usun(listbox, zadanie))
    delete_button.pack(side=LEFT, padx=10)

    done_button = Button(root, text='Mark Done', command=lambda: zaznacz(listbox, zadanie))
    done_button.pack(side=LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()

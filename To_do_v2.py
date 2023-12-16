import tkinter as tk
from tkcalendar import Calendar

def ladowanie():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def zapisz_zadania(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def dodaj_zadanie(entry, listbox, tasks):
    new_task = entry.get()
    if new_task:
        tasks.append(new_task)
        listbox.insert(tk.END, f"{len(tasks)}. {new_task}")
        zapisz_zadania(tasks)
        entry.delete(0, tk.END)

def usun_zadanie(listbox, tasks):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del tasks[index]
        listbox.delete(selected_index)
        zapisz_zadania(tasks)

def zakonczone(listbox, tasks):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = tasks[index]
        if not task.startswith("[Done] "):
            tasks[index] = f"[Done] {task}"
            listbox.delete(selected_index)
            listbox.insert(tk.END, tasks[index])
            zapisz_zadania(tasks)

def odznacz_zadanie(listbox, tasks):
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        task = tasks[index]
        if task.startswith("[Done] "):
            tasks[index] = task[len("[Done] "):]
            listbox.delete(selected_index)
            listbox.insert(tk.END, tasks[index])
            zapisz_zadania(tasks)

def dodaj_zadanie_do_daty(calendar, entry, listbox, tasks):
    selected_date = calendar.selection_get()
    if selected_date:
        new_task = entry.get()
        if new_task:
            formatted_date = selected_date.strftime("%Y-%m-%d")
            tasks.append(f"{formatted_date}: {new_task}")
            listbox.insert(tk.END, f"{len(tasks)}. {formatted_date}: {new_task}")
            zapisz_zadania(tasks)
            entry.delete(0, tk.END)

def otworz_kalendarz(entry, listbox, tasks):
    # Funkcja do obs³ugi przycisku "Otwórz kalendarz"
    def dodaj_zadanie_z_kalendarza():
        dodaj_zadanie_do_daty(cal, entry, listbox, tasks)
        cal_window.destroy()

    # Tworzenie okna kalendarza
    cal_window = tk.Toplevel()
    cal_window.title('Wybierz date')

    # Tworzenie wid¿etu kalendarza
    cal = Calendar(cal_window, selectmode='day')
    cal.pack(padx=10, pady=10)

    # Przycisk dodawania zadania do wybranej daty
    add_task_button = tk.Button(cal_window, text='Dodaj zadanie', command=dodaj_zadanie_z_kalendarza)
    add_task_button.pack(pady=10)

    # Obs³uga zdarzenia zamkniêcia okna kalendarza
    cal_window.protocol("WM_DELETE_WINDOW", lambda: cal_window.destroy())

def main():
    try:
        window_h = 600
        window_w = 500

        root = tk.Tk()
        root.title('ToDo List')
        root.geometry(f"{window_w}x{window_h}")

        tasks = ladowanie()

        listbox = tk.Listbox(root, selectbackground='Gold', font=('Helvetica', 12), height=15, width=(window_w))
        listbox.pack(pady=10)

        for i, task in enumerate(tasks, start=1):
            listbox.insert(tk.END, f"{i}. {task}")

        entry = tk.Entry(root, width=40)
        entry.pack(pady=10)

        add_button = tk.Button(root, text='Dodaj zadanie', command=lambda: dodaj_zadanie(entry, listbox, tasks))
        add_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(root, text='Usun zadanie', command=lambda: usun_zadanie(listbox, tasks))
        delete_button.pack(side=tk.LEFT, padx=10)

        done_button = tk.Button(root, text='Zakonczone', command=lambda: zakonczone(listbox, tasks))
        done_button.pack(side=tk.LEFT, padx=10)

        undo_button = tk.Button(root, text='Odznacz', command=lambda: odznacz_zadanie(listbox, tasks))
        undo_button.pack(side=tk.LEFT, padx=10)

        calendar_button = tk.Button(root, text='Otworz kalendarz', command=lambda: otworz_kalendarz(entry, listbox, tasks))
        calendar_button.pack(side=tk.LEFT, padx=10)

        root.mainloop()
    except Exception as e:
        print(f"Wystapil blad: {e}")

if __name__ == "__main__":
    main()

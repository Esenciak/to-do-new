from tkinter import *

def wczytaj_zadania():
    try:
        with open('zadania.txt', 'r') as plik:
            zadania = [linia.strip().split(" | ") for linia in plik.readlines()]
        return zadania
    except FileNotFoundError:
        return []

def zapisz_zadania(zadania):
    with open('zadania.txt', 'w') as plik:
        for zadanie in zadania:
            plik.write(" | ".join(zadanie) + "\n")

def dodaj_zadanie(entry, listbox, zadania, kryteria):
    nowe_zadanie = entry.get()
    if nowe_zadanie:
        kryteria_entry = [k.get() for k in kryteria]
        zadania.append([nowe_zadanie] + kryteria_entry)
        listbox.insert(END, f"{len(zadania)}. {nowe_zadanie}")
        zapisz_zadania(zadania)
        entry.delete(0, END)
        for k in kryteria:
            k.delete(0, END)

def usun_zadanie(listbox, zadania):
    indeks_wybrany = listbox.curselection()
    if indeks_wybrany:
        indeks = indeks_wybrany[0]
        del zadania[indeks]
        listbox.delete(indeks)
        zapisz_zadania(zadania)

def oznacz_wykonane(listbox, zadania):
    indeks_wybrany = listbox.curselection()
    if indeks_wybrany:
        indeks = indeks_wybrany[0]
        zadanie = zadania[indeks]
        if not zadanie[0].startswith("[Wykonane] "):
            zadania[indeks][0] = f"[Wykonane] {zadanie[0]}"
            listbox.delete(indeks)
            listbox.insert(END, zadania[indeks][0])
            zapisz_zadania(zadania)

def main():
    root = Tk()
    root.title('Lista Zadañ')
    root.geometry('500x400')

    zadania = wczytaj_zadania()

    listbox = Listbox(root, selectbackground='Gold', font=('Helvetica', 12), height=15, width=50)
    listbox.pack(pady=10)

    for i, zadanie in enumerate(zadania, start=1):
        listbox.insert(END, f"{i}. {zadanie[0]}")

    entry = Entry(root, width=50)
    entry.pack(pady=10)

    kryteria_label = Label(root, text="Kryteria:", font=('Helvetica', 12))
    kryteria_label.pack()

    kryteria = []
    for i in range(4):
        k = Entry(root, width=50)
        k.pack()
        kryteria.append(k)

    dodaj_button = Button(root, text='Dodaj Zadanie', command=lambda: dodaj_zadanie(entry, listbox, zadania, kryteria))
    dodaj_button.pack(side=LEFT, padx=10)

    usun_button = Button(root, text='Usuñ Zadanie', command=lambda: usun_zadanie(listbox, zadania))
    usun_button.pack(side=LEFT, padx=10)

    wykonane_button = Button(root, text='Oznacz Wykonane', command=lambda: oznacz_wykonane(listbox, zadania))
    wykonane_button.pack(side=LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()

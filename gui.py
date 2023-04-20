import bundestag as bt
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# Konfiguration des Fensters
root.title("Suchbegriff eingeben")
root.geometry("600x400")
root.resizable(False, False)
root.configure(background="#F0F0F0")

# Label-Komponente
label = tk.Label(root, text="Suchbegriff eingeben:", font=("Helvetica", 14), bg="#F0F0F0", fg="#333333")
label.pack(pady=20)

# Eingabeaufforderung
entry = tk.Entry(root, font=("Helvetica", 14), bg="#FFFFFF", fg="#333333", bd=0, relief=tk.SOLID)
entry.pack(ipady=10)
# Funktion, um die Eingabe zu lesen und eine Nachrichtbox anzuzeigen
def search():
    search_term = entry.get()
    messagebox.showinfo("Suche gestartet", f"Gefunden: {bt.anzahl_von('MDB_STAMMDATEN.xml', search_term)}")
    messagebox.showinfo("Suche gestartet", f"Gefunden: \n{bt.abge_name_list('MDB_STAMMDATEN.xml', search_term)}")
#To do
# Button-Komponente
button = tk.Button(root, text="Suche starten", font=("Helvetica", 14), bg="#333333", fg="#FFFFFF", command=search)
button.pack(pady=20)

# Event-Listener für das Return-Ereignis
def on_return(event):
    search()

# Event-Listener hinzufügen
entry.bind('<Return>', on_return)

# # Dropdown-Menü-Komponente
# option_var = tk.StringVar()
# option_menu = tk.OptionMenu(root, option_var, "Optionen", "Vorname", "Nachname", "Alter", "Geburtsdatum", "Sterbedatum", "Geschlecht", "Geburtsland", "Beruf")
# option_menu.pack()

# # Funktion, um die ausgewählten Optionen zu lesen
# def check():
#     options = []
#     for i in range(1,9):
#         if vars()[f"cb{i}"].get() == 1:
#             options.append(option_menu["menu"].entrycget(i, "label"))
#     print(f"Ausgewählte Optionen: {options}")

# # Schalter-Optionen für das Dropdown-Menü
# cb1 = tk.IntVar()
# cb2 = tk.IntVar()
# cb3 = tk.IntVar()
# cb4 = tk.IntVar()
# cb5 = tk.IntVar()
# cb6 = tk.IntVar()
# cb7 = tk.IntVar()
# cb8 = tk.IntVar()

# option_menu["menu"].add_separator()
# option_menu["menu"].add_checkbutton(label="Vorname", variable=cb1, onvalue=1, offvalue=0, command=check)
# option_menu["menu"].add_checkbutton(label="Nachname", variable=cb2, onvalue=1, offvalue=0, command=check)
# option_menu["menu"].add_checkbutton(label="Alter", variable=cb3, onvalue=1, offvalue=0, command=check)
# option_menu["menu"].add_checkbutton(label="Geburtsdatum", variable=cb4, onvalue=1, offvalue=0, command=check)
# option_menu["menu"].add_checkbutton(label="Sterbedatum", variable=cb5, onvalue=1, offvalue=0, command=check)
# option_menu["menu"].add_checkbutton(label="Geschlecht", variable=cb6, onvalue=1, offvalue=0, command=check)
# option_menu["menu"].add_checkbutton(label="Geburtsland", variable=cb7, onvalue=1, offvalue=0, command=check)
# option_menu["menu"].add_checkbutton(label="Beruf", variable=cb8, onvalue=1, offvalue=0, command=check)

# # Button-Komponente
# button = tk.Button(root, text="Aktion", command=check)
# button.pack(pady=20)


root.mainloop()

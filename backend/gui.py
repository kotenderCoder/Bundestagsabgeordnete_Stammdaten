import bundestag as bt
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
bundesdata = bt.Bundesdata('backend/MDB_STAMMDATEN.xml')
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
    messagebox.showinfo("Ergebnis", f"{bundesdata.suche_anzahl(search_term)}")
    messagebox.showinfo("Ergebnis", f"\n{bundesdata.suche_data_list(search_term)}")
    messagebox.showinfo("Ergebnis", f"\n{bundesdata.suche_grouped(search_term)}")

#To do
# Button-Komponente
button = tk.Button(root, text="Suche starten", font=("Helvetica", 14), bg="#333333", fg="#FFFFFF", command=search)
button.pack(pady=20)

#TODO Check buttons
switch_alter = tk.Checkbutton(root)
switch_partei = tk.Checkbutton(root)
switch_alter.pack(pady=10)
switch_partei.pack(pady=10)
# Event-Listener für das Return-Ereignis
def on_return(event):
    search()

# Event-Listener hinzufügen
entry.bind('<Return>', on_return)


root.mainloop()

import bundestag as bt
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
bundesdata= bt.Bundesdata('backend/MDB_STAMMDATEN.xml')
# Konfiguration des Fensters
root.title("Suchbegriff eingeben")
root.geometry("600x400")
root.resizable(False, False)
root.configure(background="#F0F0F0")

# Label-Komponente
label = tk.Label(root, text="Suchbegriff eingeben:", font=("Helvetica", 14), bg="#F0F0F0", fg="#333333")
label.pack(pady=20)
def search():
    search_term = entry.get()
    messagebox.showinfo("Ergebnis", f"{bundesdata.suche_anzahl(search_term)}")
    messagebox.showinfo("Ergebnis", f"\n{bundesdata.suche_data_list(search_term)}")
    messagebox.showinfo("Ergebnis", f"\n{bundesdata.suche_grouped(search_term)}")

# Eingabeaufforderung
entry = tk.Entry(root, font=("Helvetica", 14), bg="#FFFFFF", fg="#333333", bd=0, relief=tk.SOLID)
entry.pack(ipady=10)
# # Button-Komponente
button = tk.Button(root, text="Suche starten", font=("Helvetica", 14), bg="#333333", fg="#FFFFFF", command=search)
button.pack(pady=20)
# label = tk.Label(root, text="Wahlperiode auswählen:", font=("Helvetica", 14), bg="#F0F0F0", fg="#333333")
# label.pack(pady=20)

# # Liste der Zahlen von 1 bis 20
# numbers = list(range(1, 21))
# def on_dropdown_change(*args):
#     wp = selected_number.get()
#     bundesdata.change_wp(wp)

# selected_number = tk.StringVar(root)
# # selected_number.set("20")
# selected_number.trace("w", on_dropdown_change)
# label.pack()

# dropdown = tk.OptionMenu(root, selected_number, *numbers)
# dropdown.pack()
#TODO Check buttons
# switch_alter = tk.Checkbutton(root)
# switch_partei = tk.Checkbutton(root)
# switch_alter.pack(pady=10)
# switch_partei.pack(pady=10)
# Funktion, um die Eingabe zu lesen und eine Nachrichtbox anzuzeigen
    

# Event-Listener für das Return-Ereignis
def on_return(event):
    search()

# Event-Listener hinzufügen
entry.bind('<Return>', on_return)


root.mainloop()

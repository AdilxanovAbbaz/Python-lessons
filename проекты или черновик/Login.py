import tkinter as tk
from tkinter import messagebox
import sqlite3



#Sql
conn = sqlite3.connect("basa.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        name TEXT,
        surname TEXT,
        t_jili TEXT,
        gmail TEXT,
        password TEXT NOT NULL
    )
""")
conn.commit()
conn.close()



root = tk.Tk()
root.title("Login / Sign in")
root.geometry("400x500")

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()



#Main страница (Главный Страница)
def Main_Window():
    clear_window()
    tk.Button(root, text="Sign In", width=25, command=open_register).pack(pady=10)
    tk.Button(root, text="Log In", width=25, command=open_login).pack(pady=10)





#Regisratsiya
def open_register():
    clear_window()
    tk.Label(root, text="Register", font=("Arial", 14)).pack(pady=10)

    entries = {}

    fields = [
        ("login", "Login"),
        ("name", "Ati"),
        ("surname", "Familya"),
        ("t_jili", "T-jili"),
        ("gmail", "Gmail"),
    ]

    for key, label in fields:
        row = tk.Frame(root)
        tk.Label(row, text=label, width=22, anchor='w').pack(side="left")
        entry = tk.Entry(row, width=25)
        entry.pack(side="left")
        entries[key] = entry
        row.pack(pady=5)

    row_pass = tk.Frame(root)
    tk.Label(row_pass, text="Parol", width=22, anchor='w').pack(side="left")
    entry_pass = tk.Entry(row_pass, show="*", width=25)
    entry_pass.pack(side="left")
    entries["password"] = entry_pass
    row_pass.pack(pady=5)

    tekseru = tk.Frame(root)
    tk.Label(tekseru, text="Jane terin' parol", width=22, anchor='w').pack(side="left")
    entry_parol_1 = tk.Entry(tekseru, show="*", width=25)
    entry_parol_1.pack(side="left")
    entries["confirm"] = entry_parol_1
    tekseru.pack(pady=5)

    def register():
        data = {key: entry.get() for key, entry in entries.items()}

        if not all(data.values()):
            messagebox.showerror("Qate", "Toldir Qammesin!")
            return

        if data["password"] != data["confirm"]:
            messagebox.showerror("Qate", "Parol dursla")
            return

        try:
            conn = sqlite3.connect("basa.db") 
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (login, name, surname, t_jili, gmail, password)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data["login"],
                data["name"],
                data["surname"],
                data["t_jili"],
                data["gmail"],
                data["password"]
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Qabillandi", "Boldi Register")
            Main_Window()
        except sqlite3.IntegrityError:
            messagebox.showerror("Qate", "Onday login bar uje")

    def abb():
        for entry in entries.values():
            entry.delete(0, tk.END)

    knopka = tk.Frame(root)
    tk.Button(knopka, text="Save", width=15, command=register).pack(side="left", padx=10, pady=10)
    tk.Button(knopka, text="Clear", width=15, command=abb).pack(side="left", padx=10, pady=10)

    knopka.pack()
    





#Login jag'i
def open_login():
    clear_window()
    tk.Label(root, text="Kiriw", font=("Arial", 14)).pack(pady=10)

    row_login = tk.Frame(root)
    tk.Label(row_login, text="Login", width=22, anchor='w').pack(side="left")
    entry_login = tk.Entry(row_login, width=25)
    entry_login.pack(side="left")
    row_login.pack(pady=5)

    row_pass = tk.Frame(root)
    tk.Label(row_pass, text="Parol", width=22, anchor='w').pack(side="left")
    entry_pass = tk.Entry(row_pass, show="*", width=25)
    entry_pass.pack(side="left")
    row_pass.pack(pady=5)

    def login():
        login = entry_login.get()
        password = entry_pass.get()

        conn = sqlite3.connect("basa.db") 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Boldi!", f"Assalawma Aleykum, {result[2]}!")
        else:
            messagebox.showerror("Qate", "Parol libo Login qate!")
        

    tk.Button(root, text="Kiriw", command=login).pack(pady=15)
    tk.Button(root, text="Lobby ga", command=Main_Window).pack()

Main_Window()
root.mainloop()

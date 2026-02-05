import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

# ---------- DATABASE ----------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- DASHBOARD ----------
def open_dashboard(username):
    dash = tk.Toplevel()
    dash.title("Dashboard")
    dash.geometry("300x200")
    dash.resizable(False, False)

    tk.Label(dash, text=f"Welcome, {username} 👋",
             font=("Arial", 14, "bold")).pack(pady=30)

    tk.Button(dash, text="Logout", width=15,
              command=dash.destroy).pack(pady=10)

# ---------- REGISTER ----------
def open_register():
    reg = tk.Toplevel(root)
    reg.title("Register")
    reg.geometry("300x260")
    reg.resizable(False, False)

    tk.Label(reg, text="Create Account",
             font=("Arial", 14, "bold")).pack(pady=15)

    tk.Label(reg, text="Username").pack()
    reg_user = tk.Entry(reg, width=25)
    reg_user.pack(pady=5)

    tk.Label(reg, text="Password").pack()
    reg_pass = tk.Entry(reg, show="*", width=25)
    reg_pass.pack(pady=5)

    def register_user():
        username = reg_user.get()
        password = reg_pass.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return

        try:
            cursor.execute(
                "INSERT INTO users VALUES (?, ?)",
                (username, hash_password(password))
            )
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully")
            reg.destroy()  # CLOSE REGISTER WINDOW
        except:
            messagebox.showerror("Error", "Username already exists")

    tk.Button(reg, text="Register", width=18,
              command=register_user).pack(pady=20)

# ---------- LOGIN ----------
def login_user():
    username = entry_user.get()
    password = entry_pass.get()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )

    if cursor.fetchone():
        entry_user.delete(0, tk.END)
        entry_pass.delete(0, tk.END)
        open_dashboard(username)   # 🔥 REAL APP BEHAVIOR
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        entry_pass.delete(0, tk.END)

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Secure Login System")
root.geometry("360x320")
root.resizable(False, False)

tk.Label(root, text="Secure Login",
         font=("Arial", 16, "bold")).pack(pady=20)

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root, width=30)
entry_user.pack(pady=5)

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, width=30, show="*")
entry_pass.pack(pady=5)

tk.Button(root, text="Login", width=22,
          command=login_user).pack(pady=10)

tk.Button(root, text="Create New Account",
          command=open_register).pack()

root.mainloop()
conn.close()


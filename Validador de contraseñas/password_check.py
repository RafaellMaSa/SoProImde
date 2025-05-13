from email.contentmanager import raw_data_manager
from pydoc import text
from stat import ST_INO
from tabnanny import check
from textwrap import shorten
import tkinter as tk
from tkinter import END, messagebox
import re 
import hashlib
import random
import string

def validate_password(password):
    errors = []
    if len(password)< 8:
        errors.append("The password must have 8 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("The password must have at least one capital letter")
    if not re.search(r"[a-z]", password):
        errors.append("The password must have at least one lowercase letter")
    if not re.search(r"[0-9]", password):
        errors.append("The password must have at least one capital letter")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>=]", password):
        errors.append("The password must have at least one special symbol(!@#$%^&*(),.?:{|<>])")
    return errors

def secuity_strenght(password):
    rate = 0
    if len(password) >= 8: rate +=1
    if re.search(r"[A-Z]", password): rate +=1
    if re.search(r"[a-z]", password): rate +=1
    if re.search(r"[0-9]", password): rate +=1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): rate +=1

    if rate <= 2:
        return "The password is weak"
    elif rate == 3 or rate == 4:
        return "Your password is moderately strong"
    else:
        return "Your password is strong"
    
def toggle_password():
    if show_pass.get():
        entry.config(show="*")
        toggle_botn.config(text="Show")
        show_pass.set(False)
    else:
        entry.config(show="")
        toggle_botn.config(text="Hide")
        show_pass.set(True)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password():
    pwd = entry.get()
    errors = validate_password(pwd)
    strength = secuity_strenght(pwd)

    result_box.delete(0, tk.END)  # limpia el Listbox

    if errors:
        result_box.insert(tk.END, "Password is invalid:")
        for err in errors:
            result_box.insert(tk.END, f"- {err}")
    else:
        result_box.insert(tk.END, f"Password is valid.")
        result_box.insert(tk.END, f"Strength: {secuity_strenght}")
        hashed = hash_password(pwd)
        result_box.insert(tk.END, f"SHA-256 Hash:")
        result_box.insert(tk.END,hashed)

def password_generate(length=12):
    if length < 8:
        return "Too short"
    capital = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    numb = random.choice(string.digits)
    symb = random.choice("!@#$%^&*()_+[]}{|;:,.<>?")

    rest = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+[]{|;:,.<>?)", k=length - 4))

    password = list(capital+lower+numb+symb+rest)
    random.shuffle(password)

    return ''.join(password)

def use_gene():
    pass_generated = password_generate()
    entry.delete(0,tk.END)
    entry.insert(0, pass_generated)
    check_password()

window = tk.Tk()
window.title("Password Checker")
window.geometry("300x300")

label = tk.Label(window, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(window, show="*", width=30)
entry.pack()

show_pass = tk.BooleanVar(value=False)
toggle_botn = tk.Button(window, text="Mostrar", command=toggle_password)
toggle_botn.pack(pady=10)

check_btn = tk.Button(window, text="Check", command=check_password)
check_btn.pack(pady=5)

generate_botn =tk.Button(window, text="Generate Random Password",command=use_gene)
generate_botn.pack(pady=5)

result_box = tk.Listbox(window, width=40, height=10)
result_box.pack(pady=10)

window.mainloop()
    



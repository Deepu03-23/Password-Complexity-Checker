import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*, etc.).")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def on_check():
    pwd = entry.get()
    strength, suggestions = check_password_strength(pwd)
    result_label.config(text=f"Password Strength: {strength}", fg="green" if strength == "Strong" else "orange" if strength == "Moderate" else "red")

    suggestion_text.delete('1.0', tk.END)
    if suggestions:
        suggestion_text.insert(tk.END, "Suggestions:\n")
        for s in suggestions:
            suggestion_text.insert(tk.END, f"• {s}\n")

# UI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show='*', font=("Arial", 12), width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=on_check, font=("Arial", 11)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

suggestion_text = tk.Text(root, height=8, width=45, wrap=tk.WORD, font=("Arial", 10))
suggestion_text.pack(pady=10)

root.mainloop()

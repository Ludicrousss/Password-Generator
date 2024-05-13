import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

class PasswordGenerator:
    def __init__(self):
        self.default_length = 10
        self.default_complexity = 'medium'

    def generate_password(self, length=None, complexity=None):
        if length is None:
            length = self.default_length
        if complexity is None:
            complexity = self.default_complexity

        if complexity == 'low':
            charset = string.ascii_lowercase + string.digits
        elif complexity == 'medium':
            charset = string.ascii_letters + string.digits
        elif complexity == 'high':
            charset = string.ascii_letters + string.digits + string.punctuation
        else:
            raise ValueError("Invalid complexity level. Choose from 'low', 'medium', or 'high'.")

        password = ''.join(random.choice(charset) for _ in range(length))
        return password

# Function to generate password and display in GUI
def generate_password_gui():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    password = password_generator.generate_password(length=length, complexity=complexity)
    password_label.config(text="Generated Password: " + password)
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(password)  # Append the password to the clipboard

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_label.cget("text").split(":")[1].strip()  # Get the generated password
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(password)  # Append the password to the clipboard

# Create Tkinter window
root = tk.Tk()
root.title("Password Generator")

# PasswordGenerator instance
password_generator = PasswordGenerator()

# Length label and entry
length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Complexity label and dropdown menu
complexity_label = tk.Label(root, text="Select the complexity level:")
complexity_label.pack()
complexity_var = tk.StringVar(root)
complexity_var.set("medium")
complexity_dropdown = tk.OptionMenu(root, complexity_var, "low", "medium", "high")
complexity_dropdown.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

# Button to copy password to clipboard
copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard)
copy_button.pack()

# Label to display generated password
password_label = tk.Label(root, text="")
password_label.pack()

# Run the Tkinter event loop
root.mainloop()

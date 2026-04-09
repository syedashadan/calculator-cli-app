import tkinter as tk
from tkinter import messagebox
import math

# -------- Functions --------
def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operation == "add":
            result = a + b
        elif operation == "sub":
            result = a - b
        elif operation == "mul":
            result = a * b
        elif operation == "div":
            if b == 0:
                raise ZeroDivisionError
            result = a / b
        elif operation == "pow":
            result = a ** b

        result_label.config(text=f"Result: {result}")
        history_list.insert(tk.END, f"{a} {operation} {b} = {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")


def square_root():
    try:
        a = float(entry1.get())
        if a < 0:
            raise ValueError
        result = math.sqrt(a)
        result_label.config(text=f"Result: {result}")
        history_list.insert(tk.END, f"√{a} = {result}")
    except:
        messagebox.showerror("Error", "Invalid input!")


# -------- Window Setup --------
root = tk.Tk()
root.title("UltraCalc GUI")
root.geometry("400x500")

# -------- Input Fields --------
tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# -------- Buttons --------
tk.Button(root, text="Add ➕", command=lambda: calculate("add")).pack(pady=5)
tk.Button(root, text="Subtract ➖", command=lambda: calculate("sub")).pack(pady=5)
tk.Button(root, text="Multiply ✖", command=lambda: calculate("mul")).pack(pady=5)
tk.Button(root, text="Divide ➗", command=lambda: calculate("div")).pack(pady=5)
tk.Button(root, text="Power 🔢", command=lambda: calculate("pow")).pack(pady=5)
tk.Button(root, text="Square Root √", command=square_root).pack(pady=5)

# -------- Result --------
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

# -------- History --------
tk.Label(root, text="History 📜").pack()
history_list = tk.Listbox(root, height=8)
history_list.pack(fill=tk.BOTH, padx=10, pady=5)

# -------- Run App --------
root.mainloop()
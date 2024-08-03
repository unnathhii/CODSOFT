import tkinter as tk
from tkinter import messagebox

def perform_operation():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation choice.")
            return
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Choose the operation:").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']
for i, operation in enumerate(operations):
    tk.Radiobutton(root, text=operation, variable=operation_var, value=operation).grid(row=2, column=i+1, padx=5, pady=5)

tk.Button(root, text="Calculate", command=perform_operation).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()

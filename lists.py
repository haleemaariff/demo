import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation based on operation selected
def calculate():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    operation = operation_var.get()

    try:
        number1 = float(num1)
        number2 = float(num2)
        
        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "/":
            if number2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            else:
                result = number1 / number2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        label_result.config(text="Result: " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main application window
root = tk.Tk()
root.title("Simple Calculator")

# Create labels and entries for numbers and operation
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Dropdown menu for operation selection
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation is addition

operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label to display result
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main tkinter event loop
root.mainloop()

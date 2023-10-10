import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a tkinter window
root = tk.Tk()
root.title("Calculator")

# Entry field
entry = tk.Entry(root, width=50, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=40, pady=40, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", padx=40, pady=40, command=clear)
clear_button.grid(row=5, column=0, columnspan=3)

# Calculate button
equals_button = tk.Button(root, text="=", padx=40, pady=40, command=calculate)
equals_button.grid(row=5, column=3)

root.mainloop()

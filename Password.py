import tkinter as tk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    password_length = int(length_entry.get())
    generated_password = generate_password(password_length)
    result_label.config(text="Generated Password: " + generated_password)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x300")

# Label and Entry for specifying password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=20)
length_entry = tk.Entry(root,font=("Helvetica",24))
length_entry.pack(pady=20,padx=20)

# Button to generate a password
generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(root, text="",font=("Helvetica",24))
result_label.pack()

# Start the GUI main loop
root.mainloop()

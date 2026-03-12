#Exercise 1: Coding is Cool
#Marionne Jizella E. Centeno

import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Coding is Cool")
window.geometry("500x300")
window.configure(bg="#1e1e1e")

# Create text label
label = tk.Label(
    window,
    text="💻 Coding is Cool!",
    font=("Arial", 28, "bold"),
    fg="#00ffcc",
    bg="#1e1e1e"
)

label.pack(expand=True)

# Run the window
window.mainloop()


'''
Created on 05-Nov-2025

@author: HP
'''

# simple_window.py

import tkinter as tk   # Step 1: Import tkinter

# Step 2: Create a window
window = tk.Tk()

# Step 3: Add a title
window.title("My First Tkinter App")

# Step 4: Set window size
window.geometry("300x200")

# Step 5: Add a label (text on the screen)
label = tk.Label(window, text="Hello Deepika! 😊", font=("Arial", 14))
label.pack(pady=20)  # pack() places it on the window

# Step 6: Add a button
def say_hello():
    label.config(text="Button Clicked! 👋")

button = tk.Button(window, text="Click Me", command=say_hello)
button.pack()

# Step 7: Keep window open (event loop)
window.mainloop()

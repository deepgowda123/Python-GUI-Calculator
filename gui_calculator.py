import tkinter as tk

# --- Window Setup ---
window = tk.Tk()
window.title("Python Calculator 🧮")
window.geometry("300x430")
window.config(bg="#2E2E2E")

# --- Entry Field ---
entry = tk.Entry(
    window,
    width=18,
    font=('Arial', 22, 'bold'),
    borderwidth=0,
    relief='flat',
    bg="#1C1C1C",
    fg="white",
    justify='right',
    insertbackground='white'
)
entry.pack(pady=20, padx=10, ipady=10)

# --- Functions ---
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        # Handle percent intelligently
        if '%' in expression:
            # Case 1: Modulus (e.g., 8%3)
            parts = expression.split('%')
            if len(parts) == 2 and parts[1].isdigit():
                result = float(parts[0]) % float(parts[1])
            else:
                # Case 2: Percentage (e.g., 50+10%)
                expression = expression.replace('%', '/100')
                result = eval(expression)
        else:
            result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# --- Buttons Layout ---
button_frame = tk.Frame(window, bg="#2E2E2E")
button_frame.pack()

buttons = [
    ['C', '⌫', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]

# --- Create Buttons ---
for row in buttons:
    frame_row = tk.Frame(button_frame, bg="#2E2E2E")
    frame_row.pack()
    for btn_text in row:
        if btn_text == 'C':
            action = clear_entry
        elif btn_text == '=':
            action = calculate
        elif btn_text == '⌫':
            action = backspace
        else:
            action = lambda x=btn_text: button_click(x)

        # 🎨 Styling
        if btn_text in ['+', '-', '*', '/', '=', '%']:
            bg_color = "#FF9500"
            fg_color = "white"
        elif btn_text in ['C', '⌫']:
            bg_color = "#A5A5A5"
            fg_color = "black"
        else:
            bg_color = "#333333"
            fg_color = "white"

        tk.Button(
            frame_row,
            text=btn_text,
            width=4,
            height=1,
            font=('Arial', 16, 'bold'),
            bg=bg_color,
            fg=fg_color,
            activebackground="#666666",
            activeforeground="white",
            borderwidth=0,
            relief='flat',
            command=action
        ).pack(side='left', padx=5, pady=5)

window.mainloop()

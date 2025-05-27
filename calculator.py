import tkinter as tk

def click(event):
    current = str(entry.get())
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Input field
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create and place buttons in a grid
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 18), relief=tk.RIDGE, bd=5)
        btn.pack(side=tk.LEFT, expand=True, fill='both')
        btn.bind("<Button-1>", click)

# Start the GUI loop
root.mainloop()

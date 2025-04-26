# src/main.py
import tkinter as tk
from tkinter import messagebox
import pyautogui
import os
from datetime import datetime
from tkinter import *
from calculator import add, subtract, multiply, divide

def on_click(op):
        a = float(entry1.get())
        b = float(entry2.get())
        

        if op == '+':
            res = (add(a, b))
        elif op == '-':
            res = (subtract(a, b))
        elif op == '*':
            res = (multiply(a, b))
        elif op == '/':
            res = (divide(a, b))
        elif op == 'Pow':
            res = (pow(a, b))
        elif op == 'Save':
            value = output1.get()
            entry1.delete(0, tk.END)
            entry1.insert(0, value)
            entry2.delete(0, tk.END)
            
        
        elif op == 'Export':
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{now}.png"
            if not os.path.exists("assets/screenshots"):
                os.makedirs("assets/screenshots")

            # update window position with all values

            root.update_idletasks()
            x = root.winfo_rootx()
            y = root.winfo_rooty()
            w = root.winfo_width()
            h = root.winfo_height()

            screenshot = pyautogui.screenshot(region=(x, y, w, h))
            screenshot.save(f"assets/screenshots/{filename}")
            messagebox.showinfo("Export", "Screenshot saved!")

        

             

        last_result = res
        output1.config(state="normal")         # Edit
        output1.delete(0, tk.END)              # clear
        output1.insert(0, str(res))            # update
        output1.config(state="readonly")       # lock



# GUI setup
root = tk.Tk()
root.title("Python Calculator")
root.geometry("250x450")

# Label + Entry for variable 1
label1 = tk.Label(root, text="Variable 1")
label1.pack()
entry1 = tk.Entry(root, width=20)
entry1.pack(pady=5)

# Label + Entry for variable 2
label2 = tk.Label(root, text="Variable 2")
label2.pack()
entry2 = tk.Entry(root, width=20)
entry2.pack(pady=5)

# Label + Entry for result
label_result = tk.Label(root, text="Result")
label_result.pack()
output1 = tk.Entry(root, width=20, state="readonly")
output1.pack(pady=5)

# Buttons
for x in ['+', '-', '*', '/','Pow', 'Save','Export']:
    btn = tk.Button(root, text=x, width=10, command=lambda s=x: on_click(s))
    btn.pack(pady=0)
    
root.eval('tk::PlaceWindow . center')
root.mainloop()
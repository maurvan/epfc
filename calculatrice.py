### IMPORTS ###

import tkinter as tk

### INITALIZE TKINTER ###

root = tk.Tk()

### MAIN WINDOW PROPERTIES ###

root.title("Calculatrice")
root.configure(bg="white")
root.geometry("200x254")

# User can't resize window
root.resizable(False, False)

### FRAME WIDGETS ###

# Where we print the results (at the top)
top_frame = tk.Frame(root, width=200, height=50, bg="white")
top_frame.grid(row=0, column=0, columnspan=4)
top_frame.pack_propagate(False)

display = tk.Label(top_frame, text="0", anchor="e", font=("Consolas", 24), bg="white")
display.pack(fill="both", expand=True, padx=5)

# Grid for all the buttons
buttons_frame = tk.Frame(root, bg="white")
buttons_frame.grid(row=1, column=0)

### DISPLAY VALUES ###

def show(value):
    display.config(text=value)

### NUMBER BUTTONS ###

# Initialize the empty list and empty operator
digits = []
operator = None

# Create 10 functions
def choose9():
    digits.append(9)
    show(digits)

tk.Button(buttons_frame, text="9", width=5, height=2, bg="SeaGreen1", relief="flat", bd=0, command=choose9).grid(row=0, column=2, padx=5, pady=5)

def choose8():
    digits.append(8)
    show(digits)

tk.Button(buttons_frame, text="8", width=5, height=2, bg="SeaGreen1", relief="flat", bd=0, command=choose8).grid(row=0, column=1, padx=5, pady=5)

def choose7():
    digits.append(7)
    show(digits)

tk.Button(buttons_frame, text="7", width=5, height=2, bg="SeaGreen1", relief="flat", bd=0, command=choose7).grid(row=0, column=0, padx=5, pady=5)

def choose6():
    digits.append(6)
    show(digits)

tk.Button(buttons_frame, text="6", width=5, height=2, bg="SeaGreen2", relief="flat", bd=0, command=choose6).grid(row=1, column=2, padx=5, pady=5)

def choose5():
    digits.append(5)
    show(digits)

tk.Button(buttons_frame, text="5", width=5, height=2, bg="SeaGreen2", relief="flat", bd=0, command=choose5).grid(row=1, column=1, padx=5, pady=5)

def choose4():
    digits.append(4)
    show(digits)

tk.Button(buttons_frame, text="4", width=5, height=2, bg="SeaGreen2", relief="flat", bd=0, command=choose4).grid(row=1, column=0, padx=5, pady=5)

def choose3():
    digits.append(3)
    show(digits)

tk.Button(buttons_frame, text="3", width=5, height=2, bg="SeaGreen3", relief="flat", bd=0, command=choose3).grid(row=2, column=2, padx=5, pady=5)

def choose2():
    digits.append(2)
    show(digits)

tk.Button(buttons_frame, text="2", width=5, height=2, bg="SeaGreen3", relief="flat", bd=0, command=choose2).grid(row=2, column=1, padx=5, pady=5)

def choose1():
    digits.append(1)
    show(digits)

tk.Button(buttons_frame, text="1", width=5, height=2, bg="SeaGreen3", relief="flat", bd=0, command=choose1).grid(row=2, column=0, padx=5, pady=5)

def choose0():
    digits.append(0)
    show(digits)

tk.Button(buttons_frame, text="0", width=5, height=2, bg="SeaGreen4", relief="flat", bd=0, command=choose0).grid(row=3, column=0, padx=5, pady=5)

### OPERATIONS BUTTONS ###

# Addition
def add():
    print("Addition !!!")
    digits.clear() # Reset

tk.Button(buttons_frame, text="+", width=5, height=2, bg="SeaGreen1", relief="flat", bd=0, command=add).grid(row=0, column=3, padx=5, pady=5)

# Substract
def substract():
    print("Substract ---")
    digits.clear() # Reset

tk.Button(buttons_frame, text="-", width=5, height=2, bg="SeaGreen2", relief="flat", bd=0, command=substract).grid(row=1, column=3, padx=5, pady=5)

# Multiply
def multiply():
    print("Multiply xxx")
    digits.clear() # Reset

tk.Button(buttons_frame, text="*", width=5, height=2, bg="SeaGreen3", relief="flat", bd=0, command=multiply).grid(row=2, column=3, padx=5, pady=5)

# Division
def division():
    print("Division ///")
    digits.clear() # Reset

tk.Button(buttons_frame, text="/", width=5, height=2, bg="SeaGreen4", relief="flat", bd=0, command=division).grid(row=3, column=3, padx=5, pady=5)

### RESULTS BUTTON ###

def result():
    print("YOUR RESULT IS ...")

tk.Button(buttons_frame, text="=", width=12, height=2, bg="SeaGreen4", relief="flat", bd=0, command=result).grid(row=3, column=1, columnspan=2, padx=5, pady=5)

### MAIN LOOP ###

root.mainloop()
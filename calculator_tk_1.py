import tkinter as tk
from tkinter import ttk

calc = tk.Tk()
calc.title("Calculator")
calc.geometry("260x400")
calc.iconbitmap("calc_icon.ico")

display = ""

def insert_number(num):
    global display
    display += str(num)
    screen_label.config(text=display)


# To calculate
def equal():
    global display
    num = display

    count = num.count(".")
    if count > 1:
        parts = num.split('.')
        parts = [part for part in parts if part]
        num = '.'.join(parts)

    if num =="" or display ==" ":
        screen_label.config(text="")
    elif "+" in num:
        numbers = num.split("+")
        results = float(numbers[0]) + float(numbers[1])
        screen_label.config(text=f"{results}")
        display = ""
    elif "-" in num:
        numbers = num.split("-")
        results = float(numbers[0]) - float(numbers[1])
        screen_label.config(text=f"{results}")
        display = ""

    elif "x" in num:
        numbers = num.split("x")
        results = float(numbers[0]) * float(numbers[1])
        screen_label.config(text=f"{results}")
        display = ""

    elif "÷" in num:
        numbers = num.split("÷")
        try:
            results = float(numbers[0]) / float(numbers[1])
            screen_label.config(text=f"{results}")
            display = ""
        except ZeroDivisionError:
            screen_label.config(text="Error")
            display = ""
frame = tk.Frame(calc)
frame.pack()

screen_label = tk.Label(frame, text="0", bg="#ADD8E6", height=4, width=33, font=("Arial"))
screen_label.config(fg="red", font=(60))
screen_label.pack(side="left")

style_but = ttk.Style()
style_plus = ttk.Style()
style_minus = ttk.Style()
style_mul = ttk.Style()
style_div = ttk.Style()
style_but.configure("Custom.TButton", foreground="black", height=1, width=2, font=("Arial", 26, "bold"))

but_7 = ttk.Button(calc, text="7", style="Custom.TButton", command=lambda: insert_number("7"))
but_7.place(x=10, y=100)
but_8 = ttk.Button(calc, text="8", style="Custom.TButton", command=lambda: insert_number("8"))
but_8.place(x=70, y=100)
but_9 = ttk.Button(calc, text="9", style="Custom.TButton", command=lambda: insert_number("9"))
but_9.place(x=135, y=100)
style_plus.configure("plus.TButton", foreground="black", background="yellow", height=1, width=2, font=("Arial", 26, "bold"))
but_plus = ttk.Button(calc, text="+", style="plus.TButton", command=lambda: insert_number("+"))
but_plus.place(x=195, y=100)

but_4 = ttk.Button(calc, text="4", style="Custom.TButton", command=lambda: insert_number("4"))
but_4.place(x=10, y=170)
but_5 = ttk.Button(calc, text="5", style="Custom.TButton", command=lambda: insert_number("5"))
but_5.place(x=70, y=170)
but_6 = ttk.Button(calc, text="6", style="Custom.TButton", command=lambda: insert_number("6"))
but_6.place(x=135, y=170)
style_minus.configure("minus.TButton", foreground="black", background="red", height=1, width=2, font=("Arial", 26, "bold"))
but_minus = ttk.Button(calc, text="-", style="minus.TButton", command=lambda: insert_number("-"))
but_minus.place(x=195, y=170)

but_1 = ttk.Button(calc, text="1", style="Custom.TButton", command=lambda: insert_number("1"))
but_1.place(x=10, y=240)
but_2 = ttk.Button(calc, text="2", style="Custom.TButton", command=lambda: insert_number("2"))
but_2.place(x=70, y=240)
but_3 = ttk.Button(calc, text="3", style="Custom.TButton", command=lambda: insert_number("3"))
but_3.place(x=135, y=240)
style_mul.configure("mul.TButton", foreground="black", background="orange", height=1, width=2, font=("Arial", 26, "bold"))
but_mul = ttk.Button(calc, text="x", style="mul.TButton", command=lambda: insert_number("x"))
but_mul.place(x=195, y=240)

but_0 = ttk.Button(calc, text="0", style="Custom.TButton", command=lambda: insert_number("0"))
but_0.place(x=10, y=310)
but_p = ttk.Button(calc, text=".", style="Custom.TButton", command=lambda: insert_number("."))
but_p.place(x=70, y=310)
but_equal = ttk.Button(calc, text="=", style="Custom.TButton", command=lambda: equal())
but_equal.place(x=135, y=310)
style_div.configure("div.TButton", foreground="black", background="lightgreen", height=1, width=2, font=("Arial", 26, "bold"))
but_div = ttk.Button(calc, text="÷", style="div.TButton", command=lambda: insert_number("÷"))
but_div.place(x=195, y=310)

def clean():
    global display
    screen_label.config(text="")
    display = ""
but_clean = tk.Button(calc, text="CLEAN", relief="raised", bg="red", command=clean)
but_clean.pack(side="bottom")

calc.mainloop()
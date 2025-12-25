import tkinter as tk

def calculate(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b == 0:
                result_label.config(text="Cannot divide by zero")
                return
            res = a / b

        result_label.config(text=f"Result: {res}")

    except ValueError:
        result_label.config(text="Enter valid numbers")


# MAIN WINDOW
root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

# INPUTS
tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# BUTTONS
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0)
tk.Button(frame, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1)
tk.Button(frame, text="*", width=5, command=lambda: calculate("*")).grid(row=0, column=2)
tk.Button(frame, text="/", width=5, command=lambda: calculate("/")).grid(row=0, column=3)

#Result
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=40)

# START APP
root.mainloop()

import tkinter as tk

# ---------- Helpers ----------
def get_a_b():
    a = float(entry_a.get())
    b = float(entry_b.get())
    return a, b

def set_result(text: str):
    result_label.config(text=text)

def clear_all():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    set_result("Result:")
    entry_a.focus_set()

def backspace():
    w = root.focus_get()
    if isinstance(w, tk.Entry):
        current = w.get()
        if current:
            w.delete(len(current) - 1, tk.END)

def insert_text(s: str):
    """Insert into whichever Entry is focused (used by keypad buttons)."""
    w = root.focus_get()
    if not isinstance(w, tk.Entry):
        w = entry_a
        w.focus_set()
    w.insert(tk.END, s)

# ---------- Operations ----------
def calc_basic(op):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b == 0:
                set_result("Error: divide by zero")
                return
            res = a / b
        else:
            return

        set_result(f"Result: {res}")
    except ValueError:
        set_result("Error: enter valid numbers")

def calc_percent_of():
    """b% of a"""
    try:
        a, b = get_a_b()
        res = (a * b) / 100
        set_result(f"Result: {res}")
    except ValueError:
        set_result("Error: enter valid numbers")

def calc_discount():
    """a - (b% of a)"""
    try:
        a, b = get_a_b()
        res = a - (a * b) / 100
        set_result(f"Result: {res}")
    except ValueError:
        set_result("Error: enter valid numbers")

def calc_tax():
    """a + (b% of a)"""
    try:
        a, b = get_a_b()
        res = a + (a * b) / 100
        set_result(f"Result: {res}")
    except ValueError:
        set_result("Error: enter valid numbers")

# ---------- UI ----------
root = tk.Tk()
root.title("Calculator")
root.geometry("750x750")

FONT = ("Arial", 16)
BTN_FONT = ("Arial", 16)

# Inputs
tk.Label(root, text="Value (a)", font=FONT).pack(pady=(12, 4))
entry_a = tk.Entry(root, font=FONT, width=18, justify="right")
entry_a.pack(pady=(0, 10))
entry_a.focus_set()

tk.Label(root, text="Percent (b%)", font=FONT).pack(pady=(0, 4))
entry_b = tk.Entry(root, font=FONT, width=18, justify="right")
entry_b.pack(pady=(0, 12))

# Result
result_label = tk.Label(root, text="Result:", font=("Arial", 20, "bold"))
result_label.pack(pady=(0, 10))

# Action buttons
action_frame = tk.Frame(root)
action_frame.pack(pady=8)

tk.Button(action_frame, text="b% of a", font=BTN_FONT, width=10, height=2,
          command=calc_percent_of).grid(row=0, column=0, padx=6, pady=6)
tk.Button(action_frame, text="Discount", font=BTN_FONT, width=10, height=2,
          command=calc_discount).grid(row=0, column=1, padx=6, pady=6)
tk.Button(action_frame, text="Tax", font=BTN_FONT, width=10, height=2,
          command=calc_tax).grid(row=0, column=2, padx=6, pady=6)
tk.Button(action_frame, text="Clear", font=BTN_FONT, width=10, height=2,
          command=clear_all).grid(row=0, column=3, padx=6, pady=6)

# Keypad (types into focused entry)
pad_frame = tk.Frame(root)
pad_frame.pack(pady=10)

keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["0", ".", "<x|"],
]

for r, row in enumerate(keypad):
    for c, label in enumerate(row):
        if label == "<x|":
            cmd = backspace
        else:
            cmd = lambda t=label: insert_text(t)

        tk.Button(pad_frame, text=label, font=BTN_FONT, width=6, height=2,
                  command=cmd).grid(row=r, column=c, padx=8, pady=8)

# Basic math buttons (+ - * /) using a and b as numbers
math_frame = tk.Frame(root)
math_frame.pack(pady=10)

for i, op in enumerate(["+", "-", "*", "/"]):
    tk.Button(math_frame, text=op, font=BTN_FONT, width=6, height=2,
              command=lambda o=op: calc_basic(o)).grid(row=0, column=i, padx=8, pady=8)

# Keyboard shortcuts (no double-typing)
root.bind("<Return>", lambda e: calc_percent_of())   # Enter
root.bind("<Escape>", lambda e: clear_all())         # Esc

root.mainloop()

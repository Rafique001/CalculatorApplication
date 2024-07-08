# calculator_ui.py

import tkinter as tk
from calculator import Calculator


class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator")

        self.calculator = Calculator()

        self.expression = tk.StringVar()
        self.history = tk.StringVar()

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="black")
        self.frame.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.frame, textvariable=self.expression, font=('Arial', 20), bd=5, insertwidth=2,
                              width=16, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        self.history_display = tk.Text(self.frame, height=10, width=24, bg="lightgrey", font=('Arial', 12), bd=2,
                                       wrap="word")
        self.history_display.grid(row=1, column=0, columnspan=4, pady=10)
        self.history_display.config(state="disabled")

        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('C', 6, 0, 4)
        ]

        for button in buttons:
            text, row, col = button[0], button[1], button[2]
            colspan = button[3] if len(button) == 4 else 1

            btn = tk.Button(self.frame, text=text, padx=20, pady=20, font=('Arial', 18),
                            command=lambda val=text: self.on_button_click(val))
            if text == "=":
                btn.config(bg="lightblue")
            elif text == "C":
                btn.config(bg="lightcoral")

            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        for i in range(7):
            self.frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.frame.grid_columnconfigure(j, weight=1)

    def bind_keys(self):
        self.root.bind("<KeyPress>", self.on_key_press)

    def on_button_click(self, value):
        if value == "=":
            result = self.calculator.evaluate_expression()
            self.update_display(result)
            self.update_history()
        elif value == "C":
            self.calculator.clear_expression()
            self.update_display("")
        else:
            self.calculator.add_to_expression(value)
            self.update_display(self.calculator.expression)

    def on_key_press(self, event):
        key = event.char
        if key in "0123456789.+-*/":
            self.calculator.add_to_expression(key)
            self.update_display(self.calculator.expression)
        elif key == "=" or key == "\r":  # Enter key
            result = self.calculator.evaluate_expression()
            self.update_display(result)
            self.update_history()
        elif key == "\x08":  # Backspace key
            self.calculator.expression = self.calculator.expression[:-1]
            self.update_display(self.calculator.expression)
        elif key == "c" or key == "C":
            self.calculator.clear_expression()
            self.update_display("")

    def update_display(self, value):
        self.expression.set(value)

    def update_history(self):
        history_text = self.history_display.get("1.0", tk.END)
        current_text = self.calculator.expression
        self.history_display.config(state="normal")
        self.history_display.insert(tk.END, current_text + "\n")
        self.history_display.config(state="disabled")

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lite Calculator")
        self.current_expression = ""

        # Display
        self.display = tk.Entry(self, font=("Arial", 18), borderwidth=2, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        numbers = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
            ("0", 4, 1)
        ]

        for (text, row, col) in numbers:
            btn = tk.Button(self, text=text, font=("Arial", 14), width=5, height=2,
                            command=lambda t=text: self.add_number(t))
            btn.grid(row=row, column=col, sticky="nsew")

        btn_clear = tk.Button(self, text="C", font=("Arial", 14), width=5, height=2, command=self.clear)
        btn_clear.grid(row=4, column=0, sticky="nsew")

        btn_eq = tk.Button(self, text="=", font=("Arial", 14), width=5, height=2, command=self.equal)
        btn_eq.grid(row=4, column=2, sticky="nsew")

    def add_number(self, num):
        self.current_expression += num
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_expression)

    def clear(self):
        self.current_expression = ""
        self.update_display()

    def equal(self):
        try:
            self.current_expression = str(eval(self.current_expression))
        except:
            self.current_expression = "Error"
        self.update_display()

test = Calculator()

test.mainloop()

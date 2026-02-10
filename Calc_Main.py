import tkinter as tk
from Calc_widgets import CalcButton
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lite Calculator")
        self.current_expression = ""

        # Display
        self.display = tk.Entry(self, font=("Arial", 18), borderwidth=2, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        numbers = [("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
            ("0", 4, 1)]

        for (text, row, col) in numbers:
            btn = CalcButton(self, text=text,command=lambda t=text: self.add_number(t))
            btn.grid(row=row, column=col, sticky="nsew")

        btn_clear = CalcButton(self, text="C", command=self.clear)
        btn_clear.grid(row=4, column=0, sticky="nsew")

        btn_eq = CalcButton(self, text="=",command=self.equal)
        btn_eq.grid(row=4, column=2, sticky="nsew")

        ops = [("+", 1), ("-", 2), ("*", 3), ("/", 4)]
        for (op, row) in ops:
            btn = CalcButton(self, text=op,
                            command=lambda o=op: self.add_operator(o))
            btn.grid(row=row, column=3, sticky="nsew")

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

    def add_operator(self, op):
        self.current_expression += op
        self.update_display()


test = Calculator()
test.mainloop()
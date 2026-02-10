import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lite Calculator")
        self.current_expression = ""

        # Display
        self.display = tk.Entry(self, font=("Arial", 18), borderwidth=2, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
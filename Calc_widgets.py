import tkinter as tk

class CalcButton(tk.Button):
    def __init__(self, master, text, command):
        super().__init__(master, text=text, font=("Arial", 14),
                         width=5, height=2,relief="sunken" ,command=command)
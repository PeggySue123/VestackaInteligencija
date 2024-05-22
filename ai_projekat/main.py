import tkinter as tk
from tkinter import *
from drawing import *

def main():
    root = tk.Tk()
    root.title('Blockade')
    root.geometry("1200x1000")
    frame = ttk.Frame(root, padding=5)
    frame.grid()
    
    a: list[int] = []
    b: list[int] = []
    fields: list[Label] = []
    walls: list[Label] = []
    zidovi: list[Label] = []

    izborPocetnihParametara(root, frame, a, b, fields, walls, zidovi)

    root.mainloop()

main()
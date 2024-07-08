# main.py

import tkinter as tk
from calculator_ui import CalculatorUI

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()

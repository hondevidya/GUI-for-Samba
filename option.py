
from tkinter import *
import tkinter as tk

class OptionMenu(tk.OptionMenu):
    def __init__(self, *args, **kw):
        self._command = kw.get("command")
        tk.OptionMenu.__init__(self, *args, **kw)
    def addOption(self, label):
        self["menu"].add_command(label=label,
            command=tk._setit(variable, label, self._command))

if __name__ == "__main__":
    root = tk.Tk()

    variable = tk.StringVar()
    variable.set("beta")

    optionMenu = OptionMenu(root, variable, "alpha", "beta", "gamma")
    optionMenu.pack()

    btn = tk.Button(root, text="Add",
        command=lambda: optionMenu.addOption("DELTA"))
    btn.pack()

    root.mainloop()

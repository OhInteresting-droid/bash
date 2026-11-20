#!/usr/bin/env python3
# Too Many Imports
import ctypes
from math import floor
from random import randint as randint
import sys
import tkinter as tk
import tkinter.messagebox as tkmb

sys.set_int_max_str_digits(1000000000)

if sys.platform == "win32":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
    
# submit button
class Calc:

    def __init__(self):
        self.submit = tk.Tk()
        screen_width = self.submit.winfo_screenwidth()
        screen_height = self.submit.winfo_screenheight()
        self.submit.overrideredirect(True)
        self.submit.geometry(
            f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
        )
        self.submit_button = tk.Button(
            self.submit, text="Submit", command=self.math
        )
        self.quit_button = tk.Button(
            self.submit, text="Quit", command=self.submit.destroy
        )

        # kinda a Main()
        self.submit_button.pack()
        self.quit_button.pack()
        self.entry1()
        self.entry2()
        self.operand()
        self.choice()
        tk.mainloop()
        screen_width = self.submit.winfo_screenwidth()
        screen_height = self.submit.winfo_screenheight()

    # User Input
    def entry1(self):
        self.entry1 = tk.Toplevel(self.submit)
        screen_width = self.submit.winfo_screenwidth()
        screen_height = self.submit.winfo_screenheight()
        self.entry1.overrideredirect(True)
        self.entry1.geometry(
            f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
        )
        self.entry1.title("Entry 1 (x)")
        self.entry1_entry = tk.Entry(self.entry1, width=10)
        self.entry1_entry.pack()

    def entry2(self):
        self.entry2 = tk.Toplevel(self.submit)
        screen_width = self.submit.winfo_screenwidth()
        screen_height = self.submit.winfo_screenheight()
        self.entry2.overrideredirect(True)
        self.entry2.geometry(
            f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
        )
        self.entry2.title("Entry 2(y)")
        self.entry2_entry = tk.Entry(self.entry2, width=10)
        self.entry2_entry.pack()

    def operand(self):
        self.operand = tk.Toplevel(self.submit)
        screen_width = self.submit.winfo_screenwidth()
        screen_height = self.submit.winfo_screenheight()
        self.operand.overrideredirect(True)
        self.operand.geometry(
            f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
        )
        self.operand.title("Operand")
        self.operand_entry = tk.Entry(self.operand, width=10)
        self.operand_entry.pack()

    def choice(self):
        self.radio = tk.Toplevel(self.submit)
        screen_width = self.submit.winfo_screenwidth()
        screen_height = self.submit.winfo_screenheight()
        self.radio.overrideredirect(True)
        self.radio.geometry(
            f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
        )
        self.radio_var = tk.IntVar()
        self.radio_0 = tk.Radiobutton(
            self.radio, text="KABOOM", variable=self.radio_var, value=0
        )
        self.radio_1 = tk.Radiobutton(
            self.radio, text="NO RICO", variable=self.radio_var, value=1
        )
        self.radio_0.pack()
        self.radio_1.pack()

    def math(self):
        # grabbing all the user input
        try:
            opp = self.operand_entry.get().lower()
            x = float(self.entry1_entry.get())
            y = float(self.entry2_entry.get())
            math = self.operand_entry.get()
        except:
            pass
        else:
            # different opperands
            if opp == "add":
                tkmb.showinfo("Sum", f"{x} + {y} = {x+y}")
            elif opp == "sub":
                tkmb.showinfo("Difference", f"{x} - {y} = {x-y}")
            elif opp == "mult":
                tkmb.showinfo("Product", f"{x} * {y} = {x*y}")
            elif opp == "divi":
                tkmb.showinfo("Quotient", f"{x} / {y} = {x/y}")
            elif opp == "power up":
                tkmb.showinfo("Powers", f"{x} ** {y} = {x**y}")
            elif opp == "boom":
                i = 1
                x = int(floor(x))
                while x > 0:
                    tkmb.showinfo(f"{i}", f"{x} = {x**2}")
                    i += 1
                    if self.radio_var.get() == 1:
                        if len(str(x)) > 100:
                            break  # for test purposes only(will not let you out otherwise TM has to nuke it)
                    x **= 2
        
        # To make it comes back after your finished
        finally:
            self.operand_entry.delete(0, tk.END), self.entry1_entry.delete(
                0, tk.END
            ), self.entry2_entry.delete(0, tk.END)
            screen_width = self.submit.winfo_screenwidth()
            screen_height = self.submit.winfo_screenheight()
            self.submit.geometry(
                f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
            ), self.operand.geometry(
                f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
            ), self.entry1.geometry(
                f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
            ), self.entry2.geometry(
                f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
            ), self.radio.geometry(
                f"+{randint(0,screen_width - 100)}+{randint(0,screen_height - 100)}"
            )


Calc()
import os
import sys
sys.path.append(".")
import tkinter as tk
import tkinter.messagebox
from tkinter import PhotoImage, ttk
from src.delegator import Delegator

class InjectionZone:
	"""
	This module defines a user interaction subsystem representing the 
	communication medium and a single access injection point for an 
	adversary to insert an attack vector or a collection of attack vectors.
	"""
	def __init__(self):
		self.sqli_vector = None

	def __str__(self) -> str:
		return self.__class__.__name__

	def __repr__(self) -> str:
		return self.__str__()

	def on_click(self) -> str:
		result = Delegator.delegate(self.sqli_vector.get())
		match result:
			case True:
				tkinter.messagebox.showinfo(message = "User has faculty privileges")
			case False:
				tkinter.messagebox.showinfo(message = "User doesn't have faculty privileges")
			case None:
				tkinter.messagebox.showinfo(message = "Something went wrong")
			case _:
				tkinter.messagebox.showinfo(message = "User doesn't exist")

	def main(self):
		bg_colour = "#0D1319"
		font_colour = "#FFFFFF"
		font_type = "Consolas"
		title = "Secure-Behavioral Design for Run-time \n Delegation of Lateral-SQLi Attack Secure Strategies \n\n\n"
		root = tk.Tk(className = " ")
		root["background"] = bg_colour
		root.iconphoto(False, PhotoImage(file = os.getcwd() + "/src/InjectionZone/musi.png"))
		root.geometry("500x410")

		tk.Label(text = "MuSI", bg = bg_colour, font = (f"{font_type} bold", 25), fg = font_colour).pack()
		ttk.Separator(orient = "horizontal",  style = "TSeparator").pack(fill = "x")
		tk.Label(text = title, bg = bg_colour, font = (f"{font_type} italic", 12), fg = font_colour).pack()
		tk.Label(text = "In-band SQLi Payload", bg = bg_colour, font = (font_type, 11), fg = font_colour).pack()
		tk.Label(text = "(Faculty Privilege Feature)", bg = bg_colour, font = (font_type, 9), fg = font_colour).pack()

		self.sqli_vector = tk.Entry(bg = bg_colour, width = 50, font = font_type, fg = "Green")
		self.sqli_vector.pack()
		self.sqli_vector.focus()
		tk.Button(root, width = 10, highlightbackground = bg_colour, font = (font_type, 10), text = "Inject", command = self.on_click).pack(pady = 5)

		root.mainloop()
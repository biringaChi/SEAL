import sys
sys.path.append(".")
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from src.delegator import Delegator

class InjectionZone:
	"""
	This module defines a user interaction subsystem representing the 
	communication medium and a single access injection point for an 
	adversary to insert an attack vector or a collection of attack vectors.
	"""
	def __init__(self) -> None:
		self.sqli_vector = None

	def on_click(self) -> str:
		# reduce the height, width, color and text of messagebox
		result = Delegator.delegate(self.sqli_vector.get())
		match result:
			case True:
				tkinter.messagebox.showinfo(message = "User has faculty privileges")
			case False:
				tkinter.messagebox.showinfo(message = "User doesn't have faculty privileges")
			case _:
				tkinter.messagebox.showinfo(message = "Something went wrong")

	def main(self):
		bg_colour = "#0D1319"
		font_colour = "#FFFFFF"
		font_type = "Consolas"

		title = "Secure-Behavioral Design for Delegating Lateral \n In-band SQLi Attack Security Strategies \n\n\n"
		root = tk.Tk(className = " ")
		root["background"] = bg_colour
		root.geometry("600x400")

		tk.Label(text = "\u03BCSI", bg = bg_colour, font = (f"{font_type} bold", 25), fg = font_colour).pack()
		ttk.Separator(orient = "horizontal",  style='red.TSeparator').pack(fill = "x")
		tk.Label(text = title, bg = bg_colour, font = (f"{font_type} italic", 12), fg = font_colour).pack()
		tk.Label(text = "In-band SQLi Payload", bg = bg_colour, font = (font_type, 11), fg = font_colour).pack()
		tk.Label(text = "(Faculty Privilege Feature)", bg = bg_colour, font = (font_type, 9), fg = font_colour).pack()

		self.sqli_vector = tk.Entry(bg = bg_colour, width = 50, font = font_type, fg = "Green")
		self.sqli_vector.pack()
		self.sqli_vector.focus()
		tk.Button(root, width = 10, highlightbackground = bg_colour, font = (font_type, 10), text = "Inject", command = self.on_click).pack(pady = 5)

		root.mainloop()
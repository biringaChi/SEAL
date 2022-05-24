import sys
sys.path.append(".")
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from src.delegator import delegate

class UI:
	def __init__(self) -> None:
		self.sqli_vector = None

	def on_click(self) -> str:
		result = delegate(self.sqli_vector.get())
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
		intro = "Secure-Behavioral Design for Delegating Lateral \n In-band SQLi Attack Security Strategies \n\n\n"
		root = tk.Tk(className = " ")
		root["background"] = bg_colour
		root.geometry("600x400")
		bisi = tk.Label(text = "\u03BCSI", bg = bg_colour, font = ("Consolas bold", 25), fg = font_colour).pack()
		separator = ttk.Separator(orient = "horizontal",  style='red.TSeparator').pack(fill="x")
		definition = tk.Label(text = intro, bg = bg_colour, font = ("Consolas italic", 12), fg = font_colour).pack()
		sqli_attack_vector = tk.Label(text = "In-band SQLi Payload", bg = bg_colour, font = ("Consolas", 11), fg = font_colour).pack()
		sqli_attack_info = tk.Label(text = "(Faculty Privilege Feature)", bg = bg_colour, font = ("Consolas", 9), fg = font_colour).pack()
		self.sqli_vector = tk.Entry(bg = bg_colour, width = 50, font = ("Consolas"), fg = "Green")
		self.sqli_vector.pack()
		self.sqli_vector.focus()
		button = tk.Button(root, width = 10, highlightbackground = bg_colour, font = ("Consolas", 10), text = "Inject", command = self.on_click)
		button.pack(pady=5)

		root.mainloop()
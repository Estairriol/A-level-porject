import tkinter as tk, sys, os, time, sqlite3 #not all of these are used yet but they are universal to the project and so are imported in all files

class Home(tk.Frame):
	def __init__(self, manager):
		tk.Frame.__init__(self, manager) #initialises the frame
		self.manager = manager #this allows us to communicate to the manager in main
		self.type = "home"

		self.label = tk.Label(self, text="Home")
		self.label.pack()
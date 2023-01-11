import tkinter as tk
from home import Home

class Menu(tk.Menu):
	def __init__(self, manager):
		tk.Menu.__init__(self, manager)
		
		self.add_command(label = "Home", command = manager.goHome)
		self.add_command(label = "Logout", command = manager.logOut)
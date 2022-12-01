import tkinter as tk, sys, os, time, sqlite3 #not all of these are used yet but they are universal to the project and so are imported in all files

class Home:
	def __init__(self, window, manager):
		self.window = window #this allows us to make changes to the window
		self.manager = manager #this allows us to communicate to the manager in main
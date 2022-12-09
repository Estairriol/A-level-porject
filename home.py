import tkinter as tk, sys, os, time, sqlite3 #not all of these are used yet but they are universal to the project and so are imported in all files

class Home(tk.Frame):
	def __init__(self, manager):
		tk.Frame.__init__(self, manager) #initialises the frame
		self.manager = manager #this allows us to communicate to the manager in main
		self.type = "home"

		self.title = tk.Label(self, text="Home", font=("Roboto", 20, "bold")) #Gives the page a title
		self.title.grid(row=0, column=0, columnspan=2)

		self.nameEnt = tk.Entry(self)#where they will search for students
		self.nameEnt.insert(0, "Enter students name:")
		self.nameEnt.grid(row=1, column=0)
		self.nameEnt.bind("<FocusIn>", self.clear)#clears the box when clicked on

		self.submitBtn = tk.Button(self, text="Submit", command=self.submit)
		self.submitBtn.grid(row=1, column=1, sticky="e")

	def submit(self):
		x=1
	
	def clear(self, e):
		self.nameEnt.delete(0, tk.END)
import tkinter as tk #not all of these are used yet but they will be in future
from login import Login #this is the login class
from home import Home #this is the homepage

class Manager: #this manages all of the pages
	def __init__(self):
		self.window = tk.Tk() #Create the window
		self.window.title("Lorem Ipsum") #Placeholder name until I think of a better one

		self.user = None
		self.loggedIn = False

		#This configures the grid in the widow
		self.window.rowconfigure(0, weight=1, minsize = 50)
		self.window.columnconfigure([0, 1, 2], minsize=20, weight=1)
		
		self.page = Login(self.window, self) #Create the login class and updates the page to login
		


		self.window.mainloop() #This is basically a while loop that runs forever and updates functions whenever needed

	def succesfullLogin(self, user): #this handles the case when the user succesfully logs in
		self.loggedIn = True
		self.user = user
		self.page = Home(self.window, self)
import tkinter as tk #not all of these are used yet but they will be in future
from login import Login #this is the login class
from home import Home #this is the homepage
from menu import Menu #this is the menu

class Manager(tk.Tk): #this manages all of the pages
	def __init__(self):
		tk.Tk.__init__(self) #Create the window
		self.frame = None #Placeholder name until I think of a better one
		
		self.title("Lorem Ipsum")

		self.user = None #this keeps a track of the user
		self.loggedIn = False #i could use self.user for this and check if it is not none
		self.page = None #This keeps track of the current page

		self.menu = Menu(self)
		#self.menu.grid(row=0, column=0)
		
		self.switchPage(Login) #Always use the switchpage method to change the page
		
		self.mainloop() #This is basically a while loop that runs forever and updates functions whenever needed

	def switchPage(self, newPage): #This function switches the page to the new page
		newFrame = newPage(self)
		if self.frame is not None:
			self.frame.destroy()
		self.frame = newFrame
		self.frame.grid(row=1, column=0)
		
	def succesfullLogin(self, user): #this handles the case when the user succesfully logs in
		self.loggedIn = True
		self.user = user
		self.switchPage(Home)

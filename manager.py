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

		self.menu = Menu(self) #initialises the menu
		self.configure(menu = self.menu) #and attaches it to the window

		self.bind("<Return>", self.handleReturnPress) #allows key pressestp be used
		
		self.switchPage(Login) #Always use the switchpage method to change the page

		self.minsize(250, 150)
		

	def switchPage(self, newPage): #This function switches the page to the new page
		newFrame = newPage(self) #creates the new frame
		if self.frame is not None:
			self.frame.destroy() #destroys the old one
		self.frame = newFrame 
		self.frame.pack() #places the new frame

		minWidth = self.frame.winfo_height()
		print(minWidth)
	
	def handleReturnPress(self, event): #this means that when enter is pressed, the deets are checked
		if self.frame.type == "login":
			self.frame.submit()
		
	def succesfullLogin(self, user): #this handles the case when the user succesfully logs in
		self.loggedIn = True
		self.user = user
		self.switchPage(Home)
	
	def goHome(self):
		self.switchPage(Home)#this is so that the menu can use this method to switch windows
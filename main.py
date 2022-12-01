import tkinter as tk, sys, os, time, sqlite3 #not all of these are used yet but they will be in future
from login import Login #this is the login class

def doNothing():#this is used as a placeholder
	pass

def main():
	window = tk.Tk() #Create the window
	window.title("Lorem Ipsum") #Placeholder name untill I think of a better one

	#This configures the grid in the widow
	window.rowconfigure(0, weight=1, minsize = 50)
	window.columnconfigure([0, 1, 2], minsize=20, weight=1)
	
	login = Login(window) #Create the login class and updates the page to login
	
	window.mainloop() #This is basically a while loop that runs forever and updates functions whenever needed

#Makes sure that this is the file being ran
if __name__ == "__main__":
	main()
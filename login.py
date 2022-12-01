import tkinter as tk, sys, os, time, sqlite3 #not all of these are used yet but they are universal to the project and so are imported in all files

def doNothing(): #placeholder
	pass

'''
CREATE TABLE IF NOT EXISTS users (
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''' #This is for me to remember what each field is

class Login(): #this manages the login page
	def __init__(self, window, manager): #this sets up the page and the buttons 
		self.window = window #this allows us to make changes to the window
		self.manager = manager #this allows us to communicate to the manager in main

		#giving the title
		self.title = tk.Label(self.window, text="Login", font=("Roboto", 20, "bold"))
		self.title.grid(row=0, column=0, columnspan=3)

		#creating the username entry box
		self.userNameLbl = tk.Label(text="Username:")
		self.userNameEnt = tk.Entry(width=20)
		self.userNameLbl.grid(row=1, column=0, sticky="e")
		self.userNameEnt.grid(row=1, column=1)

		#creating the password entry box
		self.passwordLbl = tk.Label(text="Password:")
		self.passwordEnt = tk.Entry(width=20)
		self.passwordEnt.config(show="*")
		self.passwordLbl.grid(row=2, column=0, sticky="e")
		self.passwordEnt.grid(row=2, column=1)

		#creating the buttons at the bottom
		self.submitBtn = tk.Button(text="Submit", command=self.submit)
		self.clearBtn = tk.Button(text="Clear", command=self.clear)
		self.submitBtn.grid(row=3, column=2, sticky="e")
		self.clearBtn.grid(row=3, column=1, sticky="e")

	def clear(self): #this clears the username and password fields
		self.userNameEnt.delete(0, tk.END)
		self.passwordEnt.delete(0, tk.END)
	
	def submit(self): #this handles the submit button and checks agains database
		
		with sqlite3.connect("data.db") as db: #this allows me to connect to the database
			cursor = db.cursor() #this cursor will be used to query the database

		#gets the values in boxes
		username = self.userNameEnt.get().lower()
		password = self.passwordEnt.get()
		print(username, password)

		query = """SELECT * FROM users WHERE username = ? AND password = ? """
		cursor.execute(query, (username, password)) #this query will check the database for the username and password
		results = cursor.fetchall() #this returns the results of the query
		if results:
			print("access granted")
			user = results[0][0]
			self.manager.succesfullLogin(user)
		else:
			x=1 #attempts += 1 #im not sure whether i want attempts yet.
			#might make text boxes red?
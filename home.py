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

		self.clearBtn = tk.Button(self, text="Clear", command=self.clear) #clears the cell
		self.clearBtn.grid(row=1, column=1, sticky="e")

		self.nameEnt.bind("<KeyPress>", self.submit)

		self.submit()
	
	def clear(self, e=None): #clears the box
		self.nameEnt.delete(0, tk.END)

	def submit(self, e=1):
		criteria = self.nameEnt.get()
		
		print(criteria)
		print("here")

		with sqlite3.connect("data/data.db") as db: #this allows me to connect to the database
			cursor = db.cursor() #this cursor will be used to query the database
		
		criteria = "%" + criteria + "%"
		query = """ SELECT * FROM students WHERE name LIKE ? """ # compares database with name entered ignoring case and other words in database
		cursor.execute(query, (criteria,))
		names = cursor.fetchall()
		print(names)

		self.buttons = [] #this is a list of all the buttons relating to students

		if len(names) <= 10: #so that no more than 10 names are displayed
			print("also here")
			for i in range(0, len(names)): #iterates through al of the names researched
				name = names[i][1]
				ID = names[i][0]

				self.buttons.append(tk.Button(self, text = name, command = lambda ID = ID: self.nameSelect(ID), width = 20)) #adds the button and binds command
				self.buttons[i].grid(row=2+i, column = 0, columnspan=2) #places the button
		else:
			for i in range(0,9):
				name = names[i][1]
				ID = names[i][0]
				print(i,names[i][0], name)
				self.buttons.append(tk.Button(self, text = name, command = lambda ID = ID: self.nameSelect(ID), width = 20))
				self.buttons[i].grid(row=2+i, column = 0, columnspan=2)



	def nameSelect(self, studentID):
		print(studentID)
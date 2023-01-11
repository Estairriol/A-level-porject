import tkinter as tk, sqlite3
from home import Home

class Student(tk.Frame):
    def __init__(self, manager):
        tk.Frame.__init__(self, manager)
        self.manager = manager
        self.type = "student"


        self.StudentID = manager.student

        with sqlite3.connect("data/data.db") as db: #this allows me to connect to the database
            cursor = db.cursor() #this cursor will be used to query the database
        
        query = """SELECT name FROM students WHERE studentID = ?"""
        cursor.execute(query, (str(self.StudentID),))
        
        self.name = cursor.fetchall()
        if not(self.name):
            manager.switchPage(Home)
        
        self.title = tk.Label(self, text="self.name", font=("Roboto", 20, "bold")) #Gives the page a title
        self.title.grid(row=0, column=0, columnspan=3)
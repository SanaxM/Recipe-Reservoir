import tkinter as tk
import sqlite3, tkinter.messagebox


class Recipe:
    def __init__(self, name, url):
        self.name = name
        self.url = url
    
    def getRecipe(self):
        return self.url
    
    def getName(self):
        return self.name
    
    def setRecipe(self, content):
        self.url = content
        return "Successfully Written!"
    
# class Database:
#     def __init__(self, fileName, col1, col2):
#         self.fileName = fileName
#         self.name = fileName + ".db"
#         self.col1Name = col1
#         self.col2Name = col2
        
#         connection = sqlite3.connect(self.name)
#         self.cursor = connection.cursor()
#         exCommand = "CREATE TABLE IF NOT EXISTS " + fileName + " (" + col1 + " TEXT, " + col2 + " TEXT)"
#         self.cursor.execute(exCommand)
#         connection.commit()
    
#     def retriveRows(self):
#         cursor = connection.cursor()
#         cursor.execute('SELECT * FROM ?', self.fileName)
#         rows = cursor.fetchall()
        
#         return rows
    
#     def enterRow(self, value1, value2):
#         cursor = connection.cursor()
#         cursor.execute('INSERT INTO recipes VALUES(?, ?)', (value1, value2))
#         connection.commit()
        
#     def closeDB(self):
#         connection.close()
    
    

#list of recipe objects
recipeList = []
connection = sqlite3.connect('recipes.db')
cursor = connection.cursor()                                    
cursor.execute('''CREATE TABLE IF NOT EXISTS recipes            
              (name TEXT, link TEXT)''')
connection.commit()

# test = Database("tester", "name", "age")


#function to retrieve recipe from the textbox
def retrieveName():
    recName = txtBox.get()
    
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM recipes')
    rows = cursor.fetchall()
    
    # rows = test.retriveRows()

    for row in rows:
        if row[0] == recName:
            recipeLbl["text"] = row[1]
            return True
    recipeLbl["text"] = "Could not find " + recName

def enterRecipe():
    #create new recipe object
    name, url = txtBox2.get(), urlBox.get()
    recipeList.append({name:url})
    cursor = connection.cursor()
    cursor.execute('INSERT INTO recipes VALUES(?, ?)', (name, url))
    connection.commit()
    
    tkinter.messagebox.showinfo("Status of Entry", "Success! Your recipe has been entered.")
    txtBox2.delete(0, tk.END)
    urlBox.delete(0, tk.END)
    # test.enterRow(name, url)
    

#create the window
window = tk.Tk()
window.title("Mom's Recipes")
window.geometry("1000x700")
window.resizable(width=False, height=False)

#create the title box frame
titleFrame = tk.Frame(master=window, height=350, width=500, bg='slate gray')
titleFrame.pack()

#create the title label
title = tk.Label(master=titleFrame, text="Search for a Recipe", bg='slate gray', fg='white')
title.place(x=280, y=160)
title.pack(side="top", pady=10)

#create the textbox
txtBox = tk.Entry(master=titleFrame, width=20, bg="light gray", fg="black")
txtBox.pack(pady=10, padx=200)

#create the button for searching for a recipe name
btn = tk.Button(master=titleFrame, width=10, bg='white', fg='slate gray', text="Search", command=retrieveName)
btn.pack(pady=15)

#create recipe label
recipeLbl = tk.Label(master=titleFrame, bg='white')
recipeLbl.pack(padx=200, pady=15)

# *****************************

#create a new frame
enterFrame = tk.Frame(master=window, height=350, width=500, bg='lavender')
enterFrame.pack(pady=30)

#create the second title label
title2 = tk.Label(master=enterFrame, text="Enter a New Recipe", bg='lavender', pady=15)
title2.place(x=280, y=160)
title2.pack(side="top", pady=10)

#create the textbox for entering a recipe name
txtBox2 = tk.Entry(master=enterFrame, width=20, bg="light gray", fg="black")
txtBox2.insert(0, "Name")
txtBox2.pack(padx=200)

#create the textbox for the URL
urlBox = tk.Entry(master=enterFrame, width=20, bg="light gray", fg="black")
urlBox.insert(0, "URL")
urlBox.pack(padx=200, pady=15)

#create the button for entering a new recipe
btn2 = tk.Button(master=enterFrame, width=10, bg='white', fg='black', text="Enter", command=enterRecipe)
btn2.pack(pady=15)

window.mainloop()

# deploying the app: https://pyinstaller.org/en/stable/
        
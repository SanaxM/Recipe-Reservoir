import tkinter as tk
import sqlite3, tkinter.messagebox
import webbrowser

#connect to the database
connection = sqlite3.connect('recipes.db')
cursor = connection.cursor()
#if the database doesn't exist, create it with a two-columned table
cursor.execute('''CREATE TABLE IF NOT EXISTS recipes            
              (name TEXT, link TEXT)''')
#save the changes
connection.commit()


#function to retrieve recipe from the textbox
def retrieveName():
    #retrieve the item name
    recName = txtBox.get()
    
    #create a cursor obj to fetch all the rows of the table in the database 
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM recipes')
    rows = cursor.fetchall()
    
    #search the tuples in the rows for the corresponding link to the item name
    for row in rows:
        if row[0] == recName:
            #paste the url onto the gui
            recipeLbl["text"] = row[1]
            #open the link in the default browser
            if "https" in row[1]:
                webbrowser.open_new_tab(row[1])
            #return true to exit the function
            return True
    #if no link is found, display the sentiment on the gui
    recipeLbl["text"] = "Could not find " + recName

def enterRecipe():
    #retrieve the name & url from the entry boxes
    name, url = txtBox2.get(), urlBox.get()
    #create a cursor obj to add the entered values to the database
    cursor = connection.cursor()
    cursor.execute('INSERT INTO recipes VALUES(?, ?)', (name, url))
    #save the changes
    connection.commit()
    
    #create a pop-up message that indicates success of entry
    tkinter.messagebox.showinfo("Status of Entry", "Success! Your recipe has been entered.")
    #clear the entry boxes of previous entries
    txtBox2.delete(0, tk.END)
    urlBox.delete(0, tk.END)  

#function to display all recipe names
def displayRecipes():
    #connect to the database & fetch all the data
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM recipes')
    rows = cursor.fetchall()
    
    #create the default string to amend
    tempStr = "Entered Recipes:\n"
    #add every name in the database to the string
    for row in rows:
        tempStr += row[0] + "\n"
    
    #display the string on the screen
    recipeLbl["text"] = tempStr

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

# ***************************** #

#create the entry frame
enterFrame = tk.Frame(master=window, height=350, width=500, bg='lavender')
enterFrame.pack(pady=30)

#create the entry title label
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

#display the recipe names
displayRecipes()

#open the window on start
window.mainloop()

        

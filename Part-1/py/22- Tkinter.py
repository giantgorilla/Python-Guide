#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter


# In[3]:


#Window Features

#Create Window
window = tkinter.Tk()
#Window Size
window.minsize(width = 450, height = 300)

def click_Button():
    userInput = my_entry.get()
    print(userInput)
    
#Label Features

my_label = tkinter.Label(text = "Type Field", font = ("Arial", 30, "bold"))
my_label.config(fg = "black")
#my_label.pack()
#my_label.pack(side = "top")
#my_label.place(x = 0, y = 0 )
#place = pack
my_label.grid(row = 0, column = 0)

#Button Features

my_button = tkinter.Button(text = "Click", command = click_Button)
#my_button.pack()
#my_button.place(x =225-63, y =150-14 )
my_button.grid(row = 0, column = 2)

#Entry - Input Features

my_entry = tkinter.Entry(width = 20)
#my_entry.place(x = 300, y = 200)
#my_entry.pack()
my_entry.grid(row = 0, column = 1)


# In[4]:


window.mainloop()


# # Widget Examples

# In[7]:


from tkinter import *


# In[38]:


window = Tk()
window.title("Tkinter Python")
window.minsize(width = 600, height = 600)
window.config(padx = 20, pady = 20)

#Label
label = Label(text = "My Label")
label.config(bg ="black")
label.config(fg= "white")
label.config(padx = 10, pady = 10)
label.pack()


def buttonClicked():
    print(text.get("1.0", END)) #1. index x'inci satırdan itibaren başlatır.
    
#Button
button = Button(text = "Button", command = buttonClicked)
button.config(padx = 10, pady = 10)
button.pack()

#Entry
entry = Entry(width = 20)
entry.pack()

#Multiline
text = Text(width = 30,height = 10)
text.focus()
text.pack()

"""#Scale
def scaleSelected(value):
    print(value)
    
scale = Scale(from = 0, to = 50, command = scaleSelected)
scale.pack
    
scale = Scale (from _= 1, to = 50)
scale.pack"""

"""#Spinbox
def spinboxSelected():
    print(spinBox.get())
    
spinbox = Spinbox(from _= 0, to = 50, command = spinboxSelected)
spinbox.pack()"""

#Check Button
def checkbuttonSelected():
    pass

checkState = IntVar()
checkButton = Checkbutton(text = "check", variable = checkState, command = checkbuttonSelected)
checkButton.pack()

#Radio Button
def radioSelected():
    print(radioCheckedState.get())
    
radioCheckedState = IntVar()
radioButton = Radiobutton(text = "1. Option", value = 10, variable = radioCheckedState, command = radioSelected)
radioButton2 = Radiobutton(text = "2. Option", value = 20, variable = radioCheckedState, command = radioSelected)
radioButton.pack()
radioButton2.pack()

#Listbox

def listBoxSelected(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox()
nameList = ["Doğukan", "Bostancı", "ABC", "QWKEK", "LOOOP"]
for i in range(len(nameList)):
    listbox.insert(i.nameList[i])
    
listbox.bind('<<ListBoxSelected>>', listBoxSelected)
listbox.pack()


window.mainloop()


# In[ ]:





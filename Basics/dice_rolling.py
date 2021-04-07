import random
from tkinter import *

root=Tk()
root.geometry("700x500")
root.title("\U0001F3B2 Dice Game") #window title

l1=Label(root,font=("times",250),foreground="CYAN") #dice/label
l1.place(x = 240, y = 50)
def roll():
    
    number=['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] #unicodes for dices
    l1.config(text=random.choice(number))
    #l1.pack()

b1=Button(root,text="Roll",font=(200),width=10,border=(1),foreground="white",background="grey",command=roll) #button
b1.place(x=320,y=30)

root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:38:18 2023

@author: kmmal
"""

 # from tkinter import *

#root=Tk()
#root.title("gift generator")
#root.geometry("400x400")

#list=['poster','chocolate','cards','flowers','ball']

#print(list)
#['poster','chocolate','cards','flowers','ball']

#import random
#random_num = random.randint(1,5)
#print(random_num)

#def show():

    #list["text"] = " listed items : ['poster','chocolate','cards','flowers','ball'] " + str(show)
   # random_num["text"] = " Put item number " + str(show) + " in the bag"
    
   # btn=Button(root,text="wich item to put in basket",command=show)
    #btn.place(relx=0.5,rely=0.4,anchor=CENTER)

#root.mainloop()


from tkinter import *
import random

root = Tk()
root.title("gift generator")
root.geometry("400x400")

items = ['poster', 'chocolate', 'cards', 'flowers', 'ball']
random_num = random.randint(1, 5)

def show():
    list_label["text"] = f"listed items: {items}"
    random_label["text"] = f"Put item number {random_num} in the bag"

list_label = Label(root, text="")
list_label.place(relx=0.5, rely=0.3, anchor=CENTER)

random_label = Label(root, text="")
random_label.place(relx=0.5, rely=0.5, anchor=CENTER)

btn = Button(root, text="Which item to put in basket", command=show)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()


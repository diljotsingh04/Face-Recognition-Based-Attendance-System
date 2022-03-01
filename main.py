from tkinter import *
import tkinter.messagebox as tmsg
import os

def aboutus():
    tmsg.showinfo("About us","This project is made in python by Diljot Singh")

def quitapp():
    MsgBox = tmsg.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       base.destroy()
    # else:
    #     tmsg.showinfo('Return','You will now return to the application screen')

def rate():
    # tmsg.askquestion("Rate us","Do you like our Project")
    from fedbwithfunc import gui

def conatactus():
    tmsg.showinfo("Contact Us","Email:-example@exmple.com")

def mainsys():
    # print("main button")
    os.startfile(r"attendance project.py")

# for making gui window
base = Tk()
window_width = 718
window_height = 475
base.geometry(f"{window_width}x{window_height}")
base.minsize(718,475)
base.maxsize(718,475)
base['background']='black'
base.title("Face Recognition based Attendace System | Diljot Singh")
base.iconbitmap("icons/faceReco.ico")

# making menubar
# mymenu = Menu(base)
# making dropdown menu
# m1 = Menu(mymenu)   #, tearoff=0
# m1.add_command(label="About Us")
# m1.add_separator()
# m1.add_command(label="About Us")
# m1.add_separator()
# m1.add_command(label="About Us")
# mymenu.add_cascade(label="File", menu=m1)

# m2 = Menu(mymenu, tearoff=0)
# m2.add_command(label="Exit", command=quit)
# mymenu.add_cascade(label="Quit", menu=m2)

#making simple menu label
# mymenu.add_command(label="Exit", command=quit)
# base.config(menu=mymenu)

#writing title
text =  Label(text="Face Recognition Attendance System", bg="black", fg="white", pady=14, font="comicsansms 20 bold", borderwidth=3, relief=SUNKEN)
text.pack(fill=X)

# frame for the buttons
f0 = Frame(base, pady=90, background='black')
f0.pack()
# making buttons
b1 = Button(f0, text="Mark Attendance", width=17, height=2, font="lucida 10 bold", relief=SOLID, command=mainsys)
b2 = Button(f0, text="Contact Us", width=17, height=2, font="lucida 10 bold", relief=SOLID, command=conatactus)
b3 = Button(f0, text="About Us", width=17, height=2, command=aboutus, font="lucida 10 bold", relief=SOLID)
b4 = Button(f0, text="Exit", width=17, height=2, command=quitapp, font="lucida 10 bold", relief=SOLID)
# packing the buttons
b1.pack(pady=2)
b2.pack(pady=2)
b3.pack(pady=2)
b4.pack(pady=2)

# rate us button
rate = Button(text="Rate Us",font="lucida 7 bold", relief=SOLID, padx=5,pady=8, command=rate)
rate.pack(side=RIGHT, padx=18,pady=10)

base.mainloop()
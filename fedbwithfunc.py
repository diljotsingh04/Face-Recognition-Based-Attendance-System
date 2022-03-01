from tkinter import *


def gui():
    def getvals():
        # print("{uservalue.get()},{passvalue.get()},{slider.get()}")

        with open("feedback record/feedback.csv","a") as f:
            f.write(f"{userentry.get()},{passentry.get()},{slider.get()}/5\n")
        feedback.destroy()

    def reset():
        uservalue.set("")
        passvalue.set("")
        slider.set(0)

    
    # size of window
    feedback = Tk()
    feedback.geometry("220x200")
    feedback.minsize(220,200)
    feedback.maxsize(220,200)
    feedback.iconbitmap("icons/Rating.ico")

    #creating label & packing
    frameen = Frame(feedback)
    frameen.grid()
    text = Label(frameen,text="Feedback", font="comicsansms 15 bold")
    user = Label(frameen, text="Name:-", font="comicsansms 10 bold")
    password = Label(frameen, text="Email:-", font="comicsansms 10 bold")
    rate = Label(frameen, text="RateUs:-", font="comicsansms 10 bold")
    slider = Scale(frameen, from_=0, to=5, orient=HORIZONTAL, tickinterval=1)
    text.grid(column=1)
    user.grid(row=1)
    password.grid(row=2)
    rate.grid(row=3)
    slider.grid(row=3, column=1)


    # value of input
    uservalue = StringVar()
    passvalue = StringVar()
    # making for inputing the value
    userentry = Entry(frameen, textvariable = uservalue, font="comicsansms 9 ")
    passentry = Entry(frameen, textvariable = passvalue, font="comicsansms 9 ")
    # griding
    userentry.grid(row=1, column=1)
    passentry.grid(row=2, column=1)
    # for button

    framefe = Frame(feedback)
    framefe.grid(row=5)
    submit = Button(framefe,text="Submit", width=7, height=1, font="lucida 8 bold", relief=SOLID, command=getvals)
    submit.grid(row=1, column=0, padx=9)
    submit = Button(framefe, text="Reset", width=7, height=1, font="lucida 8 bold", relief=SOLID, command=reset)
    submit.grid(row=1, column=1, padx=9)

    feedback.mainloop()


gui()
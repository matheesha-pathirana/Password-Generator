from random import *
from tkinter import *

num="0123456789"
alphanum="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spalphanum="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

# passlen = int(input("Enter Password Length \n"))
# randpass = []

# print("select the type of password \n1. Numbers\n2. Alphanum\n3. Special Alphanumeric\n")
# selecttype = int(input())

# if selecttype == 1:
#     for i in range(passlen):
#         randpass.append(choice(num))
# elif selecttype == 2:
#     for i in range(passlen):
#         randpass.append(choice(alphanum))
# else:
#     for i in range(passlen):
#         randpass.append(choice(spalphanum))

# result = "".join(randpass)

# print("Your Random Password Is : "+result)


def create_pass():

    Thechoice = Tchoice.get()

    if Thechoice=="":
        resultBox.delete(0.0,END)
        resultBox.insert(END,"\n Select The Type Of Password You Like")
    
    length = int(pass_length.get())
    randpass = []
    for i in range(length):
        randpass.append(choice(Thechoice))

    result ="".join(randpass)

    TheResult = "\n *** Your Password Is : "+result+" ***\n"

    resultBox.delete(0.0,END)
    resultBox.insert(END,TheResult)






window = Tk()
window.geometry("800x500")
window.title("Password Generator BY Matheesha Pathirana ⚆_⚆")

progname = Label(window,font=('Consolas',15,'bold'),text="Password Generator BY Matheesha Pathirana :D",fg="blue")
progname.grid(row=1,column=3,padx=180,pady=30)

chooseType = Label(window,font=('Consolas',15,'bold'),text="Choose a Type Among the 3")
chooseType.place(relx=.02, rely=.3)

Tchoice = StringVar()
numchoice = Radiobutton(window,font=('Arial',10,'bold'),text ="Numeric", variable = Tchoice,value=num)
numchoice.place(relx=.1, rely=.40)
alphanumchoice = Radiobutton(window,font=('Arial',10,'bold'),text ="Alphanumeric", variable = Tchoice,value=alphanum)
alphanumchoice.place(relx=.1, rely=.45)
specialchoice = Radiobutton(window,font=('Arial',10,'bold'),text ="Special", variable = Tchoice,value=spalphanum)
specialchoice.place(relx=.1, rely=.50)


size=Label(window,text="Size",font=('Arial',14,'bold'))
size.place(relx= .59 , rely= .39)

pass_length = Spinbox(window,from_=8,to=100)
pass_length.place(relx=.65,rely=.4)
pass_length.config(state="readonly")



GenButton = Button(window,font=('Arial',10,'bold'),text = "Generate",command=create_pass)
GenButton.place(relx=.45, rely=.7)

resultBox = Text(window, height=5, width = 80,)
resultBox.place(relx=.1, rely=.8)

window.mainloop()
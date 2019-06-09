from tkinter import *
from tkinter import messagebox

##함수

def myFunc() :
    if var.get() == 1:
        label1.configure(text='파이썬')
    elif var.get()==2:
        label1.configure(text='Java')
        


##메인코드
window=Tk()
var=IntVar()
rb1=Radiobutton(window, text='파이썬', variable=var, value=1,
               command=myFunc)
rb2=Radiobutton(window, text='JAVA', variable=var, value=2,
               command=myFunc)
label1=Label(window, text='', fg='red')

rb1.pack(); rb2.pack(); label1.pack()

window.mainloop()

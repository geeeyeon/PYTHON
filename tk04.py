from tkinter import *
from tkinter import messagebox

##함수
def myFunc() :
    messagebox.showinfo('강아지','귀엽니?')


##메인코드
window=Tk()

photo=PhotoImage(file='D:/imageFile/GIF/dog.gif')
button1=Button(window, image=photo, command=myFunc)


button1.pack()
window.mainloop()

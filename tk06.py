from tkinter import *
from tkinter import messagebox
window=Tk()
btnList=[None]*3

for i in range(0,3):
    btnList[i]=Button(window, text='버튼'+str(i+1))

for i in range(0,3):
    btnList[i].pack(side=RIGHT)


window.mainloop()

##클릭한 좌표 구하기 프로그램

from tkinter import *
from tkinter import messagebox

##함수선언
def clickLeft(event):
    txt=''
    if event.num==1:
        txt+='왼쪽-'
    elif event.num==2:
        txt+='가운데-'
    txt += str(event.x)+','+str(event.y)

    label1.configure(text=txt)
    

##메인 코드
window=Tk()
window.geometry('400x400')

label1=Label(window, text='나를 클릭해줘')

window.bind("<Button>", clickLeft)
label1.pack()
window.mainloop()

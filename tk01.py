from tkinter import *

window = Tk()
window.title("여기 제목")
window.geometry("400x100")
window.resizable(width=FALSE,height=FALSE)

label1=Label(window, text='Python 공부중')
label2=Label(window, text='Python 공부중', font=('궁서체',30),
            fg='blue')
label3=Label(window, text='Python 공부중', bg='megenta',
             width=20, height=5, anchor=SE)

label1.pack()
label2.pack()
label3.pack()
window.mainloop()

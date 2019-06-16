from tkinter import *
from tkinter.filedialog import*

def file_oepn():
    global filename
    filename=askopenfilename(parent=window,
                             filetypes=(("GIF파일","*.gif"),("모든파일","*.*")))
                             
##전역 변수
filename=''

##메인 코드                          
                             
window=Tk()

mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label='파일',menu=fileMenu)
fileMenu.add_command(label='열기')
fileMenu.add_separator()
fileMenu.add_command(label='종료')


window.mainloop()

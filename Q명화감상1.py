from tkinter import *
from tkinter.filedialog import*
##확대 축소

def func_open():
    global filename
    filename=askopenfilename(parent=window,
                             filetypes=(("GIF파일","*.gif"),("모든파일","*.*")))
    photo=PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_exit():
    window.quit()
    window.destroy()

def func_zoom():
    global filename, inH, inW, outH, outW, canvas,paper
    outW=inW; outH=inH
    sclae=askinteger('확대','값 입력',minvalue=2,maxvalue=5)
    outImage=[]
    for i in range(0,inW):
        tmpList=[]
    for k in range(0,inH):
        tmpList.append(0)
        out.Image.append(tmpList)
    for i in range(0,inW):
        for k in range(0,inH):
            outImage[i][k]=inImage[i][k]
    displayImage()


def func_sub():
    pass

filename=''



##메인 코드                          
                             
window=Tk()
window.geometry("400x400")
window.title("명화 감상")

photo=PhotoImage()
pLabel=Label(window,image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label='파일',menu=fileMenu)
fileMenu.add_command(label='열기',command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label='종료',command=func_exit)


imageMenu=Menu(mainMenu)
mainMenu.add_cascade(label='이미지 효과',menu=imageMenu)
fileMenu.add_command(label='확대하기',command=func_zoom)
fileMenu.add_command(label='축소하기',command=func_sub)


window.mainloop()

###회전하기
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import os.path
import math

## 함수 선언부
def loadImage(fname) :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    inImage = []
    fsize = os.path.getsize(fname)
    inH = inW = int(math.sqrt(fsize))
    fp = open(fname, 'rb')
    for i in range(0,inW) :
        tmpList = []
        for k in range(0, inH) :
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
    fp.close()
    
def displayImage() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    winW = inW + outW
    if outH > inH :
        winH = outH
    else :
        winH = inH
    
    if canvas != None :
        canvas.destroy()
    window.geometry(str(winW) + 'x' + str(winH))
    canvas = Canvas(window, width = winW, height = winH)
    paper = PhotoImage(width = winW, height = winH)
    canvas.create_image( (winW / 2, winH / 2), image=paper, state='normal')
    
    for i in range(0, inW) :
        for k in range(0, inH) :
            data = inImage[i][k]
            paper.put("#%02x%02x%02x" % (data,data, data), (k,i))
    for i in range(0, outW) :
        for k in range(0, outH) :
            data = outImage[i][k]
            paper.put("#%02x%02x%02x" % (data,data, data), (k+inW,i))    
    canvas.pack()
    
def func_open() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    filename = askopenfilename(parent=window,
            filetypes=(("RAW파일","*.raw"), ("모든파일","*.*")))
    if filename == '' or filename == None :
        return
    loadImage(filename) # 파일 --> 메모리 (inImage, inH, inW)
    displayImage() # 메모리 -->화면
    

    
    
    
def func_save() :
    pass
def func_exit() :
    pass
def photo_equal() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정.
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0,inW) :
        tmpList = []
        for k in range(0, inH) :
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘 ###
    for i in range(0, inW) :
        for k in range(0, inH) :
            outImage[i][k] = inImage[i][k]
    ###############################
    displayImage()
    
def photo_add() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    value = askinteger('밝게', '값 입력')    
    # 출력 파일의 크기 결정.
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0,inW) :
        tmpList = []
        for k in range(0, inH) :
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘 ###
    for i in range(0, inW) :
        for k in range(0, inH) :
            outImage[i][k] = inImage[i][k] + value
    ###############################
    displayImage()
def photo_sub() :
    pass
def photo_reverse() :
    pass
def photo_zoomin() : #확대
    pass
def photo_zoomout() : #축소
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    scale = askinteger('축소', '값 입력', minvalue=2, maxvalue=16)    
    # 출력 파일의 크기 결정.
    outW = int(inW/scale); outH = int(inH/scale)
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0,outW) :
        tmpList = []
        for k in range(0, outH) :
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘 ###
    for i in range(0, inW) :
        for k in range(0, inH) :
            outImage[int(i/scale)][int(k/scale)] = inImage[i][k] 
    ###############################
    displayImage()

## 전역 변수 선언부
window, canvas, filename, paper = [None] * 4
inImage, outImage = [], [] 
inW, inH, outW, outH = [0] * 4

## 메인 코드

window = Tk(); window.title('그레이 포토샵 ver 0.01')
mainMenu = Menu(window);  window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='파일 열기', command=func_open)
fileMenu.add_command(label='파일 저장', command=func_save)
fileMenu.add_command(label='종료', command=func_exit)

photo1Menu=Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=photo1Menu)
photo1Menu.add_command(label='동일영상', command=photo_equal)
photo1Menu.add_command(label='밝게하기(덧셈)', command=photo_add)
photo1Menu.add_command(label='어둡게하기(뺄셈)', command=photo_sub)
photo1Menu.add_command(label='반전하기', command=photo_reverse)

photo2Menu=Menu(mainMenu)
mainMenu.add_cascade(label='영상처리2', menu=photo2Menu)
photo2Menu.add_command(label='축소', command=photo_zoomout)
photo2Menu.add_command(label='확대', command=photo_zoomin)

window.mainloop()







    

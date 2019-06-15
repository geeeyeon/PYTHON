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
    
def displayImage(image, w, h, sp) :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    for i in range(0, w) :
        for k in range(0, h) :
            data = image[i][k]
            paper.put("#%02x%02x%02x" % (data,data, data), (k+sp,i))
    
    
def func_open() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    filename = askopenfilename(parent=window,
            filetypes=(("RAW파일","*.raw"), ("모든파일","*.*")))
    if filename == '' or filename == None :
        return
    if canvas != None :
        canvas.destroy()
    loadImage(filename) # 파일 --> 메모리 (inImage, inH, inW)
    window.geometry(str(inW*2) + 'x' + str(inH))
    canvas = Canvas(window, width = inW*2, height = inH)
    paper = PhotoImage(width = inW*2, height = inH)
    canvas.create_image( (inW , inH / 2), image=paper, state='normal')
    displayImage(inImage, inH, inW, 0) # 메모리 -->화면
    canvas.pack()

    
    
def func_save() :
    pass
def func_exit() :
    pass
def photo_equal() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    #출력파일의 크기 결정
    outW = inW; outH = inH
    #출력 영상 메모리 확보
    outImage = []
    for i in range(0,inW) :
        tmpList = []
        for k in range(0, inH) :
            tmpList.append(0)
        outImage.append(tmpList)
    ###진짜 영상처리 알고리즘###
    for i in range(0, inW):
        for k in range(0,inH):
            outImage[i][k] = inImage[i][k]
    ###########################
    displayImage(outImage, outW, outH, inW) 

    
def photo_add() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    #출력파일의 크기 결정
    outW = inW
    outH = inH
    value=0
    value = askinteger('밝게(덧셈)','값(1~255)을 입력하세요',minvalue=1, maxvalue=255)
    #출력 영상 메모리 확보
    outImage = []
    for i in range(0,inW) :
        tmpList = []
        for k in range(0, inH) :
            tmpList.append(0)
        outImage.append(tmpList)
    ###진짜 영상처리 알고리즘###
    for i in range(0, inW):
        for k in range(0,inH):
            outImage[i][k]=inImage[i][k]+value
            if outImage[i][k] > 255:
                outImage[i][k]=255
            else :
                outImage[i][k]=inImage[i][k]+value
    ###########################
    displayImage(outImage, outW, outH, inW) 
def photo_sub() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    #출력파일의 크기 결정
    outW = inW
    outH = inH
    value=0
    value = askinteger('어둡게(뺄셈)','값(1~255)을 입력하세요',minvalue=1, maxvalue=255)
    #출력 영상 메모리 확보
    outImage = []
    for i in range(0,inW) :
        tmpList = []
        for k in range(0, inH) :
            tmpList.append(0)
        outImage.append(tmpList)
    ###진짜 영상처리 알고리즘###
    for i in range(0, inW):
        for k in range(0,inH):
            outImage[i][k]=inImage[i][k]-value
            if outImage[i][k] < 0:
                outImage[i][k]=0
            else :
                outImage[i][k]=inImage[i][k]-value
    ###########################
    displayImage(outImage, outW, outH, inW) 
def photo_reverse() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    #출력파일의 크기 결정
    outW = inW
    outH = inH
    #출력 영상 메모리 확보
    outImage = []
    for i in range(0,inW) :
        tmpList = []
        for k in range(0, inH) :
            tmpList.append(0)
        outImage.append(tmpList)
    ###진짜 영상처리 알고리즘###
    for i in range(0, inW):
        for k in range(0,inH):
            outImage[i][k]=255 - inImage[i][k]
          
    ###########################
    displayImage(outImage, outW, outH, inW) 

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

window.mainloop()

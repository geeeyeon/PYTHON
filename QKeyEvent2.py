##photoshop에 단축키 추가하
#퀴즈에서 구현한 것들을 키보드로 처리하기
from tkinter import *
from tkinter import messagebox


## 함수 선언

def loadImage(fname) :
    global window, canvas, paper, inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')
    for i in range(0,XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data =  int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image) :
    global window, canvas, paper, inImage, XSIZE, YSIZE
    for i in range(0, XSIZE) :
        for k in range(0, YSIZE) :
            data = inImage[i][k]
            paper.put("#%02x%02x%02x"%(data, data, data), (k,i))


def keyEvent(event):
    print('keyEvent 들어옴')
    if chr(event.keycode).upper() == 'U' :
        brightImage()
    elif chr(event.keycode).upper()=='R' :
        rotateImage()
    elif chr(event.keycode).upper()=='M' :
        mirroImage()


def brightImage():
    print('** 밝아지기 실행 **')
    for i in range(0,XSIZE):
        for k in range(0,YSIZE):
            value=inImage[i][k]
            value=value+100
            if value>255:
                value=255
            inImage[i][k]=value
    displayImage(inImage)


def rotateImage():
    print('$$$ 회전하기 $$$')


def mirroImage():
    tmp=0
    for i in range(0,XSIZE):
        for k in range(0,int(YSIZE/2)):
            tmp = inImage[i][k]
            inImage[i][k]=inImage[i][255-k]
            inImage[i][255-k]=tmp
    displayImage(inImage)
    

## 전역(Global) 변수 선언

window, canvas, paper = [None] *3
XSIZE, YSIZE = 0, 0
inImage=[]

## 메인 코드

size = int(input('크기(128/256/512):'))
XSIZE=YSIZE=size
window = Tk()
window.title("그레이 사진 보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper=PhotoImage(width=YSIZE, height=XSIZE)
canvas.create_image( (XSIZE/2,YSIZE/2),image=paper,state='normal')




# 파일 --> 메모리

filename = input('파일명-->')
loadImage(filename)

window.bind("<Key>",keyEvent)

# 메모리 --> 화면

displayImage(inImage)
canvas.pack()
window.mainloop()

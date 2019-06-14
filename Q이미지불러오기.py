#퀴즈3. 512x512영상을 보여라
from tkinter import *
##함수선언
def loadImage(fname):
    global window, canvas, paper, inImage, XSIZE, YSIZE
    fp=open(fname, 'rb')
    for i in range(0,XSIZE) :
        tmpList = []
        for k in range(0,YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image):
    global window, canvas, paper, inImage, XSIZE, YSIZE
    for i in range(0,XSIZE):
        for k in range(0,YSIZE):
            data = inImage[i][k]
            paper.put("#%02x%02x%02x"%(data,data,data),(k,i))
            


##전역(Global)변수선언
window, canvas, paper = [None]*3
XSIZE, YSIZE = 512,512
inImage=[]

##메인 코드
window = Tk()
window.title("그레이사진보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper=PhotoImage(width=YSIZE, height=XSIZE)
canvas.create_image( (XSIZE/2, YSIZE/2), image=paper, state='normal')

#파일 --> 메모리
filename='d:/raw/512/LENNA512.raw'
loadImage(filename)

#메모리-->화면
displayImage(inImage)

canvas.pack()
window.mainloop()

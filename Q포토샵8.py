##08:수평/수직 에지검출, 1차미분에지, 1차미분 회선, 라플라시안회선, LoG,DoG
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
     global window, canvas, paper, photo, photo2, oriX, oriY
    if photo2 == None :
        return
    saveFp=asksaveasfile(parent=window, mode="w", defaulttextension=".jpg",
                         filetypes=(("JPG 파일", "*.jpg; *.jpeg"), ("모든 파일", "*.*")))
    savePhoto = photo2.convert("jpg")
    savePhoto.save(filename=saveFp.name)
def func_exit() :
    window.quit()
    window.destroy()
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

def photo_rotate1() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    degree=askinteger('각도','값 입력',minvalue=0, maxvalue=360)
    #출력파일의 크기 결정
    outW=inW; outH=inH
    #출력영상메모리확보
    outImage=[]
    for i in range(0,inW) :
        tmpList=[]
        for k in range(0,inH) :
            tmpList.append(0)
        outImage.append(tmpList)
    #진짜영상처리 알고리즘
    radian=degree * 3.141592 / 180.0
    for i in range(0,inW) :
        for k in range(0, inH):
            xs=i; ys=k
            xd = int(math.cos(radian)*xs - math.sin(radian)*ys)
            yd = int(math.sin(radian)*xs + math.cos(radian)*ys)
            if 0 <= xd < outW and 0 <= yd < outH :
                outImage[xd][yd]=inImage[xs][ys]
        ###########################
    displayImage(outImage, outW, outH, inW)

def photo_rotate2():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    degree=askinteger('각도','값 입력',minvalue=0, maxvalue=360)
    #출력파일의 크기 결정
    outW=inW; outH=inH
    #출력영상메모리확보
    outImage=[]
    for i in range(0,inW) :
        tmpList=[]
        for k in range(0,inH) :
            tmpList.append(0)
        outImage.append(tmpList)
    #진짜영상처리 알고리즘
    radian=degree * 3.141592 / 180.0
    cx=int(inW/2); cy=int(inH/2)
    for i in range(0,outW) :
        for k in range(0, outH):
            xs=i; ys=k
            xd = int(math.cos(radian)*(xs-cx)
                     - math.sin(radian)*(ys-cy))+cx
            yd = int(math.sin(radian)*(xs-cx)
                     + math.cos(radian)*(ys-cy))+cy
            if 0 <= xd < outW and 0 <= yd < outH :
                outImage[xs][ys]=inImage[xd][yd]
        ###########################
    displayImage(outImage, outW, outH, inW)


def photo_morphing() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    percent = askinteger('비율', '값 입력(0-100)', minvalue=0, maxvalue=100)
   # 출력 파일의 크기 결정.
    outW = inW; outH = inH
    # 영상 선택.
    filename = askopenfilename(parent=window,
            filetypes=(("RAW파일","*.raw"), ("모든파일","*.*")))
    if filename == '' or filename == None :
        return
    inImage2 = []
    fsize = os.path.getsize(filename)
    inH2 = inW2 = int(math.sqrt(fsize))
    fp = open(filename, 'rb')
    for i in range(0,inW2) :
        tmpList = []
        for k in range(0, inH2) :
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage2.append(tmpList)
    fp.close()
    
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
            value = int( (inImage[i][k]*(100-percent)*0.01 + inImage2[i][k]*percent*0.01)/2)
            if value > 255 :
                outImage[i][k] = 255
            elif value < 0 :
                outImage[i][k] = 0
            else :
                outImage[i][k] = value
            
    ###############################
    displayImage(outImage, outW, outH, inW)


def photo_embo():
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
    ##엠보싱 마스크 준비
    mSize=3
    mask=[ [-1,0,0],[0,0,0],[0,0,1] ]
    ######
    #임시 입력 영상 +2
    tmpInImage = []
    for i in range(0,inW+2) :
        tmpList = []
        for k in range(0,inH+2) :
            tmpList.append(127)
        tmpInImage.append(tmpList)
    #임시 출력 영상
    tmpOutImage = []
    for i in range(0,outW) :
        tmpList = []
        for k in range(0,outW) :
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    #입력 ==> 임시 입력
    for i in range(0, inW) :
        for k in range(0,inH) :
            tmpInImage[i+1][k+1] = inImage[i][k]
    #회선 연산
    for i in range(0, inW):
        for k in range(0, inH):
            #1점에 대해서 3x3마스크 연산 ->모두 곱해서 더하기
            s = 0.0
            for m in range(0,mSize) :
                for n in range(0,mSize) :
                    s +=mask[m][n] * tmpInImage[i+m][k+n]
            tmpOutImage[i-1][k-1]=s

    #결과값 처리(0<, 255>, mask 합계가 0이면 어두움)
    for i in range(0,outW):
        for k in range(0,outH) :
            tmpOutImage[i][k] += 127.0
    #임시 출력->출력
    for i in range(0,outW):
        for k in range(0, outH):
            if tmpOutImage[i][k]<0:
                outImage[i][k]=0
            elif tmpOutImage[i][k]>255:
                outImage[i][k]=255
            else :
                outImage[i][k]=int(tmpOutImage[i][k])
    ###########################
    displayImage(outImage, outW, outH, inW) 

def photo_blurr():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### 엠보싱 마스크 
    mSize = 3
    mask = [ [1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9] ]
    #################################
    ### 임시 입력 영상 + 2개
    tmpInImage = []
    for i in range(0, inW + 2):
        tmpList = []
        for k in range(0, inH + 2):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    #입력 ==> 임시 입력
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+1][k+1] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            #1점에 대해서 3x3마스크 연산 ->모두 곱해서 더하기
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_sharp():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### 엠보싱 마스크 
    mSize = 3
    mask = [ [0, -1, 0], [-1, 5, -1], [0, -1, 0] ]
    #################################
    ### 임시 입력 영상 + 2개
    tmpInImage = []
    for i in range(0, inW + 2):
        tmpList = []
        for k in range(0, inH + 2):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    #입력 ==> 임시 입력
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+1][k+1] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            #1점에 대해서 3x3마스크 연산 ->모두 곱해서 더하기
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_gau():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### 엠보싱 마스크 
    mSize = 3
    mask = [ [1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16] ]
    #################################
    ### 임시 입력 영상 + 2개
    tmpInImage = []
    for i in range(0, inW + 2):
        tmpList = []
        for k in range(0, inH + 2):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    #입력 ==> 임시 입력
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+1][k+1] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            #1점에 대해서 3x3마스크 연산 ->모두 곱해서 더하기
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_onhpfsharp():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### 엠보싱 마스크 
    mSize = 3
    mask = [ [-1, -1, -1], [-1, 8, -1], [-1, -1, -1] ]
    #################################
    ### 임시 입력 영상 + 2개
    tmpInImage = []
    for i in range(0, inW + 2):
        tmpList = []
        for k in range(0, inH + 2):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    #입력 ==> 임시 입력
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+1][k+1] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            #1점에 대해서 3x3마스크 연산 ->모두 곱해서 더하기
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_hedge():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### 엠보싱 마스크 
    mSize = 3
    mask = [ [0, -1, 0], [0, 1, 0], [0, 0, 0] ]
    #################################
    ### 임시 입력 영상 + 2개
    tmpInImage = []
    for i in range(0, inW + 2):
        tmpList = []
        for k in range(0, inH + 2):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    #입력 ==> 임시 입력
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+1][k+1] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            #1점에 대해서 3x3마스크 연산 ->모두 곱해서 더하기
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_vedge():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### 엠보싱 마스크 
    mSize = 3
    mask = [ [0, 0, 0], [-1, 1, 0], [0, 0, 0] ]
    #################################
    ### 임시 입력 영상 + 2개
    tmpInImage = []
    for i in range(0, inW + 2):
        tmpList = []
        for k in range(0, inH + 2):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    #입력 ==> 임시 입력
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+1][k+1] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            #1점에 대해서 3x3마스크 연산 ->모두 곱해서 더하기
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_laplacian():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW; outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### 엠보싱 마스크 
    mSize = 3
    mask = [ [0, 1, 0], [1, -4, 1], [0, 1, 0] ]
    #################################
    ### 임시 입력 영상 + 2개
    tmpInImage = []
    for i in range(0, inW + 2):
        tmpList = []
        for k in range(0, inH + 2):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    #입력 ==> 임시 입력
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+1][k+1] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            #1점에 대해서 3x3마스크 연산 ->모두 곱해서 더하기
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_LoG():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW
    outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### log 마스크 
    mSize = 5
    mask = [ [0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0] ]
    #################################
    ### 임시 입력 영상 + 2개
    tmpInImage = []
    for i in range(0, inW + 4):
        tmpList = []
        for k in range(0, inH + 4):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    ### 입력 > 임시 입력 붙이기
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+2][k+2] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            # 한 점에 대해서 3x3 마스크 연산 > 모두 곱해서 더하기 > 이 결과 s에 저장
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_DoG1():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW
    outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### dog 7x7 마스크 
    mSize = 7
    mask = [ [0, 0, -1, -1, -1, 0, 0], [0, -2, -3, -3, -3, -2, 0], [-1, -3, 5, 5, 5, -3, -1], [-1, -3, 5, 16, 5, -3, -1], [-1, -3, 5, 5, 5, -3, -1], [0, -2, -3, -3, -3, -2, 0], [0, 0, -1, -1, -1, 0, 0]]
    #################################
    ### 임시 입력 영상 
    tmpInImage = []
    for i in range(0, inW + 6):
        tmpList = []
        for k in range(0, inH + 6):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    ### 입력 > 임시 입력 붙이기
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+3][k+3] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            # 한 점에 대해서 3x3 마스크 연산 > 모두 곱해서 더하기 > 이 결과 s에 저장
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    displayImage(outImage, outW, outH, inW)

def photo_DoG2():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    outW = inW
    outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    ### dog 9x9 마스크 
    mSize = 9
    mask = [ [0, 0, 0, -1, -1, -1, 0, 0, 0],
             [0, -2, -3, -3, -3, -3, -3, -2, 0],
             [0, -3, -2, -1, -1, -1, -2, -3, 0],
             [-1, -3, -1, 9, 9, 9, -1, -3, -1],
             [-1, -3, -1, 9, 19, 9, -1, -3, -1],
             [-1, -3, -1, 9, 9, 9, -1, -3, -1],
             [0, -3, -2, -1, -1, -1, -2, -3, 0],
             [0, -2, -3, -3, -3, -3, -3, -2, 0],
             [0, 0, 0, -1, -1, -1, 0, 0, 0] ]
    #################################
    ### 임시 입력 영상 
    tmpInImage = []
    for i in range(0, inW + 8):
        tmpList = []
        for k in range(0, inH + 8):
            tmpList.append(127)
        tmpInImage.append(tmpList)
    ### 임시 출력 영상
    tmpOutImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        tmpOutImage.append(tmpList)
    ### 입력 > 임시 입력 붙이기
    for i in range(0, inW):
        for k in range(0, inH):
            tmpInImage[i+3][k+3] = inImage[i][k]
    ### 회선 연산 
    for i in range(1, inW):
        for k in range(1, inH):
            # 한 점에 대해서 3x3 마스크 연산 > 모두 곱해서 더하기 > 이 결과 s에 저장
            s = 0.0
            for m in range(0, mSize):
                for n in range(0, mSize):
                    s += mask[m][n] * tmpInImage[i+m][k+n]
                tmpOutImage[i-1][k-1] = s
    ### tmpOutImage > outImage
    for i in range(0, outW):
        for k in range(0, outH):
            if tmpOutImage[i][k] < 0 :
                outImage[i][k] = 0
            elif tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
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

photo2Menu=Menu(mainMenu)
mainMenu.add_cascade(label='영상처리2', menu=photo2Menu)
photo2Menu.add_command(label='동일영상', command=photo_equal)
photo2Menu.add_command(label='회전하기', command=photo_rotate1)
photo2Menu.add_command(label='역방향', command=photo_rotate2)

photo3Menu=Menu(mainMenu)
mainMenu.add_cascade(label='영상처리3', menu=photo3Menu)
photo3Menu.add_command(label='동일영상', command=photo_equal)
photo3Menu.add_command(label='모핑', command=photo_morphing)
photo3Menu.add_command(label='엠보싱', command=photo_embo)

photo4Menu=Menu(mainMenu)
mainMenu.add_cascade(label='화소처리1',menu=photo4Menu)
photo4Menu.add_command(label='블러링',command=photo_blurr)
photo4Menu.add_command(label='샤프닝',command=photo_sharp)
photo4Menu.add_command(label='가우시안',command=photo_gau)
photo4Menu.add_command(label='고주파샤프닝',command=photo_onhpfsharp)

photo5Menu=Menu(mainMenu)
mainMenu.add_cascade(label='화소처리2',menu=photo5Menu)
photo5Menu.add_command(label='수평에지',command=photo_hedge)
photo5Menu.add_command(label='수직에지',command=photo_vedge)
photo5Menu.add_command(label='라플라시안회선',command=photo_laplacian)
photo5Menu.add_command(label='LoG',command=photo_LoG)
photo5Menu.add_command(label='7x7DoG',command=photo_DoG1)
photo5Menu.add_command(label='9x9DoG',command=photo_DoG2)

window.mainloop()



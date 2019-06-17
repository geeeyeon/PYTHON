# 퀴즈3. 회전 후 영상 모두 보이도
# ch9 29 아래공식 ) 새 중점 맞추기필요함
# 새 중점 ) 29 공식으로 만든 사이즈의 틀을 tmpinput으로 만들고
# p34 보고해봐
# tmpinput에 원래 input을 넣고 돌리기
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import os.path
import math

## 함수 선언
def loadImage(fname) :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paer, filename
    inImage = []
    fsize = os.path.getsize(fname)      # 파일 크기 아는 함수
    inH = inW = int(math.sqrt(fsize))    # 입력 파일의 폭과 높이(파일 크기에서 루트 씌우면 알 수 있음)
    fp = open(fname, 'rb')
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
    fp.close()

def displayImage() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    winW = inW + outW
    if outH > inH:
        winH = outH
    else:
        winH = inH
        
    if canvas != None :
        canvas.destroy()
    window.geometry(str(winW) + 'x' + str(winH))
    
    canvas = Canvas(window, width = winW, height = winH)
    paper = PhotoImage(width = winW, height = winH)
    canvas.create_image((winW / 2, winH / 2), image=paper, state='normal')
    
    canvas.pack()
    for i in range(0, inW) :
        for k in range(0, inH) :
            data = inImage[i][k]
            paper.put("#%02x%02x%02x" % (data,data, data), (k, i))
    for i in range(0, outW) :
        for k in range(0, outH) :
            data = outImage[i][k]
            paper.put("#%02x%02x%02x" % (data,data, data), (k+inW, i))
    canvas.pack()
    
def func_open() :
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    filename = askopenfilename(parent=window, filetypes=(("RAW파일","*.raw"), ("모든파일","*.*")))
    if filename == '' or filename == None :
        return
    
    loadImage(filename) # 파일 --> 메모리 (inImage, inH, inW)
    displayImage() # 메모리 -->화면
    
def func_save():
    pass

def func_exit():
    pass

# 영상처리1
def Photo_equal():
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
    for i in range(0, inW):
        for k in range(0, inH):
            outImage[i][k] = inImage[i][k]
    displayImage()
    

def Photo_bright():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    scale = askinteger('밝게', '값 입력')
    # 출력 파일의 크기 결정
    outW = inW
    outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    for i in range(0, inW):
        for k in range(0, inH):
            outImage[i][k] = inImage[i][k] + scale
            if outImage[i][k] > 255:
                outImage[i][k] = 255
    displayImage()

def Photo_dark():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    scale = askinteger('어둡게', '값 입력')
    # 출력 파일의 크기 결정
    outW = inW
    outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    for i in range(0, inW):
        for k in range(0, inH):
            outImage[i][k] = inImage[i][k] - scale
            if outImage[i][k] < 0:
                outImage[i][k] = 0
    displayImage()

def Photo_reverse():
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
    for i in range(0, inW):
        for k in range(0, inH):
            value = inImage[i][k]
            value = 255 - value
            outImage[i][k] = value
    displayImage()

# 영상처리2
def Photo_zoomout():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    scale = askinteger('축소', '값 입력')
    # 출력 파일의 크기 결정
    outW = int(inW/scale)
    outH = int(inH/scale)
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    for i in range(0, outW):
        for k in range(0, outH):
            outImage[i][k] = inImage[i*2][k*2]
    displayImage()

def Photo_zoomin():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    # 출력 파일의 크기 결정
    if inH == 256:
        scale = askinteger('확대', '값 입력(max = 2)', minvalue = 1, maxvalue = 2)
    elif inH == 128:
        scale = askinteger('확대', '값 입력(max = 4)', minvalue = 1, maxvalue = 4)
    outW = int(inW*scale)
    outH = int(inH*scale)
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        outImage.append(tmpList)
    ### 진짜 영상 처리 알고리즘!!! ###
    for i in range(0, outW):
        for k in range(0, outH):
            outImage[i][k] = inImage[int(i/scale)][int(k/scale)]
    displayImage()

def Photo_rotate1():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    degree = askinteger('회전', '값 입력(0~360)', minvalue = 0, maxvalue = 360)
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
    #Radian = degree * 3.141592 / 180.0              # degree 값을 radian으로 변경
    radian = math.radians(degree)
    for i in range(0, inW):
        for k in range(0, inH):
            xs = i
            ys = k
            xd = int(math.cos(radian) * xs - math.sin(radian) * ys)
            yd = int(math.sin(radian) * xs + math.cos(radian) * ys)
            if 0 <= xd < outW and 0 <= yd < outH:
                outImage[xd][yd] = inImage[xs][ys]
    displayImage()

def Photo_rotate2():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    degree = askinteger('회전', '값 입력(0~360)', minvalue = 0, maxvalue = 360)
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
    #Radian = degree * 3.141592 / 180.0              # degree 값을 radian으로 변경
    radian = math.radians(degree)
    for i in range(0, outW):
        for k in range(0, outH):
            xs = i
            ys = k
            xd = int(math.cos(radian) * xs - math.sin(radian) * ys)
            yd = int(math.sin(radian) * xs + math.cos(radian) * ys)
            if 0 <= xd < outW and 0 <= yd < outH:
                outImage[xs][ys] = inImage[xd][yd]
    displayImage()

def Photo_rotate3():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    degree = askinteger('회전', '값 입력(0~360)', minvalue = 0, maxvalue = 360)
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
    #Radian = degree * 3.141592 / 180.0              # degree 값을 radian으로 변경
    radian = math.radians(degree)
    cx = int(inW/2)
    cy = int(inH/2)
    for i in range(0, outW):
        for k in range(0, outH):
            xs = i
            ys = k
            xd = int(math.cos(radian) * (xs - cx) - math.sin(radian) * (ys - cy) + cx)
            yd = int(math.sin(radian) * (xs - cx) + math.cos(radian) * (ys - cy) + cy)
            if 0 <= xd < outW and 0 <= yd < outH:
                outImage[xs][ys] = inImage[xd][yd]
            else:
                outImage[xs][ys] = 255
    displayImage()

def Photo_rotate4():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    degree = askinteger('회전', '값 입력(0~360)', minvalue = 0, maxvalue = 360)
    if degree > 270:
        degree -= 90
    if degree > 180:
        degree -= 90
    if degree > 90:
        degree -= 90
        
    radian = degree * 3.141592 / 180.0
    minusradian = (90-degree) * 3.141592 / 180.0 

    tmpW, tmpH = 0, 0
    tmpImage = []
    tmpW = int(inH * math.cos(minusradian) + inW * math.cos(radian))
    tmpH = int(inH * math.cos(radian) + inW * math.cos(minusradian))

    # 출력 파일의 크기 결정
    outW = tmpW
    outH = tmpH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, tmpW):
        tmpList = []
        for k in range(0, tmpH):
            tmpList.append(0)
        outImage.append(tmpList)

    for i in range(0, tmpW):            # 초기화
        tmpList = []
        for k in range(0, tmpH):
            tmpList.append(255)
        tmpImage.append(tmpList)

    for i in range(0, inW):
        for k in range(0, inH):
            tmpImage[i + int((tmpW-inW)/2)][k + int((tmpH-inH)/2)] = inImage[i][k]

    ### 진짜 영상 처리 알고리즘!!! ###
    cx = int(tmpW/2)
    cy = int(tmpH/2)
    rx = math.cos(radian) * inW - math.sin(radian) * inH
    ry = math.sin(radian) * inW + math.cos(radian) * inH
    for i in range(0, outW):
        for k in range(0, outH):
            xs = i
            ys = k
            xd = int( (cx + (xs - cy) * math.sin(-radian) + (ys - cx) * math.cos(radian)) )
            yd = int( (cy + (xs - cy) * math.cos(radian) - (ys - cx) * math.sin(-radian)) )
            if 0 <= xd < outW and 0 <= yd < outH:
                outImage[xs][ys] = tmpImage[xd][yd]
            else:
                outImage[xs][ys] = 255
    displayImage()

def Photo_mor():
    global inImage, outImage, inH, inW, outH, outW, window, canvas, paper, filename
    filename = askopenfilename(parent=window, filetypes=(("RAW파일","*.raw"), ("모든파일","*.*")))
    value = askinteger('비율', '첫번째 파일의 값 입력(1~9)', minvalue = 1, maxvalue = 9)
    # 출력 파일의 크기 결정
    outW = inW
    outH = inH
    # 출력 영상 메모리 확보
    outImage = []
    for i in range(0, outW):
        tmpList = []
        for k in range(0, outH):
            tmpList.append(0)
        outImage.append(tmpList)
        
    inImage2 = []
    fsize = os.path.getsize(filename)      # 파일 크기 아는 함수
    inH = inW = int(math.sqrt(fsize))    # 입력 파일의 폭과 높이(파일 크기에서 루트 씌우면 알 수 있음)
    fp = open(filename, 'rb')
    for i in range(0, inW):
        tmpList = []
        for k in range(0, inH):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage2.append(tmpList)
    fp.close()
        
    ### 진짜 영상 처리 알고리즘!!! ###
    for i in range(0, outW):
        for k in range(0, outH):
      #      value = int((inImage[i][k] + inImage2[i][k]) / 2)
            outImage[i][k] = int((inImage[i][k] * value / 10) + (inImage2[i][k] * (10 - value) / 10))
       #     outImage[i][k] = value
            if outImage[i][k] > 255:
                outImage[i][k] = 255
    displayImage()


## 전역 변수
window, canvas, filename, paper = [None] * 4
inImage, outImage = [], []
inW, inH, outW, outH = [0] * 4

## 메인 코드
if __name__ == "__main__":
    window = Tk()
    window.title("그레이 포토샵 ver 0.01")

    # 메뉴 추가
    mainMenu = Menu(window)
    window.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "파일", menu = fileMenu)
    fileMenu.add_command(label = "파일 열기", command = func_open)
    fileMenu.add_separator()
    fileMenu.add_command(label = "파일 저장", command = func_save)
    fileMenu.add_separator()
    fileMenu.add_command(label = "프로그램 종료", command = func_exit)

    photo1Menu = Menu(mainMenu)
    mainMenu.add_cascade(label = "영상처리1", menu = photo1Menu)
    photo1Menu.add_command(label = "동일영상", command = Photo_equal)
    photo1Menu.add_command(label = "밝게하기", command = Photo_bright)
    photo1Menu.add_command(label = "어둡게하기", command = Photo_dark)
    photo1Menu.add_command(label = "반전모드", command = Photo_reverse)

    photo2Menu = Menu(mainMenu)
    mainMenu.add_cascade(label = "영상처리2", menu = photo2Menu)
    photo2Menu.add_command(label = "축소", command = Photo_zoomout)
    photo2Menu.add_command(label = "확대", command = Photo_zoomin)
    photo2Menu.add_command(label = "회전1", command = Photo_rotate1)
    photo2Menu.add_command(label = "회전2(역방향)", command = Photo_rotate2)
    photo2Menu.add_command(label = "회전3(중심)", command = Photo_rotate3)
    photo2Menu.add_command(label = "회전4(이미지 안잘리게)", command = Photo_rotate4)
    photo2Menu.add_command(label = "모핑", command = Photo_mor)

    window.mainloop()

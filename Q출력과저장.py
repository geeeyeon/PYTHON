
#퀴즈2. txt파일에 숫자가 10개 써있다.
#2-1. 합계를 내서 화면에 출력한다
inSum=0
inFp=open("D:/JiYeon/number.txt","r")
while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    
    inSum+=int(inStr)

print(inSum)
inFp.close()
'''
inFp=open('D:/JiYeon/number2.txt','r')
hap=0
while True:
    inStr = inFp.readline()
    if not inStr:
        break
    inList=inStr.split()
    for num in inList:
        hap+=int(num)
print(hap)
inFp.close()
'''


#2-2.값 중에서 짝수는 even.txt.에 홀수는 odd.txt에 분리저장
num=0
inSum1=0
inSum2=0
inFp=open("D:/JiYeon/number.txt","r")
outFp1=open("D:/JiYeon/even.txt",'w')
outFp2=open("D:/JiYeon/odd.txt",'w')
while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    num=int(inStr)
    if num%0:
        inSum1+=int(inStr)
        outFp1.writelines(inSum1)
    else :
        inSum2+=int(inStr)
        outFp2.writelines(inSum2)

inFp.close()
outFp.close()




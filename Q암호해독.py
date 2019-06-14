
#전역변수선언
inFp, outFp = None, None
inStr, outStr="",""
secu = 0 #암호화:100, 암호해독 -100


#메인코드
secuYN = input ("1:암호화, 2:암호해독 -->")
inFname = input("입력파일 ->")
outFname = input("출력파일 -->")

if secuYN == "1" :
    secu=100
else :
    secu=-100


inFp = open(inFname, 'r', encoding='utf-8')
outFp = open(outFname, 'w', encoding='utf-8')

while True :
    inStr = inFp.readline()
    if not inStr:
        break
    outStr = ""
    for ch in inStr :
        
        chNum = ord(ch)
        
        if ord('0')<=chNum<=ord('9'):
            chNum=chNum
            
        else:
            chNum += secu
            
        ch2=chr(chNum)
        outStr += ch2
    outFp.writelines(outStr)

inFp.close()
outFp.close()
print('변환완료')
    

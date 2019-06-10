##별찍
i,k,star=0,0,0
numStr, ch ="",""



num=input("숫자를 여러 개 입력하세요: ")
i=0
#ch=numStr[i]
while True:
    star=int(ch)

    starStr=""
    for k in range(0,star):
        startStr += "\u2605"
        k+=1

    print(starStr)

    i+=1
    if(i>len(numStr)-1):
        break

    ch=numStr[i]

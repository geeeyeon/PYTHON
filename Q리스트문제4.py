#퀴즈5 : 위 코드를 버블 정렬로 변경, 중간에 그만두는 코드 추가
import random
myList=[]
sw=0
for i in range(0,10):
    myList.append(random.randrange(0,10))
print(myList)
for i in range(0,9):
    for k in range(0, 9-i):
        if myList[k]>myList[k+1]:
            myList[k],myList[k+1]=myList[k+1],myList[k]
        i+=1
    i=0
print(myList)

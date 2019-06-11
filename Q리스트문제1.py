#퀴즈2.myList에서 77을 모두 지우는 프로그램을 작성
find=0
for i in range(0,myList.count(77)):
    myList.remove(77)
        
print(myList)

value=1
list2=[]
for _ in range(0,3):
    tmpList=[]

    for _ in range(0,4):
        tmpList.append(value)
        value+=1
    list2.append(tmpList)

print(list2)

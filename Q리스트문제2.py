#퀴즈3. 5x3 짜리 리스트에 100,97,94,...을 채우고 192페이지처럼 출력
tmpList=[]
list2=[]
value=100
for _ in range (0,5):    
    for _ in range(0,3):
        tmpList.append(value)
        value-=3
    list2.append(tmpList)
    tmpList=[]
print(list2)

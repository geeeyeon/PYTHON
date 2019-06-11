#퀴즈6 : 랜덤(1~99)하게 5x5리스트를 만든다->1차원리스트로 만들고 정렬한다
#       ->다시 5x5리스트로 만든다
import random
myList=[]
tmpList=[]
for i in range(0,5):
    for k in range(0,5):
        tmpList.append(random.randrange(0,10))
    myList.append(tmpList)
    tmpList=[]
print(myList)
for i in range(0,5):
    for k in range(0,5):
        tmpList.append(myList)

print(tmpList)

'''
rList = []
rList2 = []
rList22 = []

for _ in range(0,5):
    r_list2 = []
    for _ in range(0,5):
        r_list2.append(random.randrange(1,100))
    rList2.append(r_list2)
print(rList2)


for i in range(0,5) :
    for k in range(0,5) :
        rList.append(rList2[i][k])
print(rList)

for i in range(0,25-1):
    for k in range(i+1, 25):
        if rList[i] > rList[k]:
           rList[i], rList[k] = rList[k], rList[i]
print(rList)

n=0
for _ in range(0,5):
    r_list22 = []
    for _ in range(0,5):
        r_list22.append(rList[n])
        n += 1
    rList22.append(r_list22)

print(rList22)
'''

#퀴즈4 3x3리스트a에 1~9까지 입력, 3x3 리스트b에 9~1까지 입력,
#  리스트c에 두 리스트 합계 넣고 출력

listA, listB, listC=[],[],[]

valueA=1
valueB=9
valueC=0
for i in range (0,3):
    tmpListA, tmpListB, tmpListC=[],[],[]
    for j in range (0,3):
        tmpListA.append(valueA)
        valueA+=1
        tmpListB.append(valueB)
        valueB-=1
        valueC=valueA+valueB
        tmpListC.append(valueC)        
    listA.append(tmpListA)
    listB.append(tmpListB)
    listC.append(tmpListC)    
print(listA)
print(listB)
print(listC)

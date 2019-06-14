#퀴즈1(Q01-01.py) : 10000부터 100000까지 789의 배수의 합계

hap=0
for i in range(10000,100000):
    if i%789==0:
        hap+=i
print(hap)
    

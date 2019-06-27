# BMI = 몸무게(KG)/(키*키)
# BMI가 18.5 이상, 25 미만일 때 표준 몸무게
# 2만명 몸무게 및 키 데이터를 사용하여 모델 생성
# 임의의 키, 몸무게가 입력되면 저체중, 정상, 비만 레이블을 출력

import random

def calc_bmi(h, w):
    bmi = w/(h/100)**2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "normal"
    return "fat"

# 출력 파일 준비
fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height,weight,label\r\n")

# 무작위 데이터 생성
cnt = {"thin":0, "normal":0, "fat":0}
for i in range(20000):
    h = random.randint(120, 200)
    w = random.randint(35, 80)
    label = calc_bmi(h,w)
    cnt[label]+=1
    fp.write("{0},{1},{2}\r\n".format(h,w,label))
fp.close()
print("파일이 잘 만들어 졌어요.", cnt)
from sklearn import svm, metrics
import glob, os.path, re, json

def check_freq(fname):
    name=os.path.basename(fname) #파일 이름만 추출
    lang=re.match(r'^[a-z]{2,}',name).group()
    # #print(name)
    # print(lang)
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower() # 소문자로 변환
    #숫자를 세는 변수(cnt) 초기화 하기
    cnt = [0 for n in range(0,26)] #c[0]=0, c[1]=0, ....
    code_a = ord("a") #a문자 아스키 코드값
    code_z = ord("z") #z문자 아스키 코드값
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z : #n에 저장된 값이 영문 소문자라면
            cnt[n-code_a]+=1
            #문자 'a'인 경우 cnt[0]에 1이 누적
            #문자 'b'인 경우 cnt[1]에 1이 누적
            #...
            #문자 'z'인 경우 cnt[25]에 1이 누적
    total = sum(cnt) # 전체 문자의 개수가 total에 저장
    freq = list(map(lambda n:n/total, cnt))
    print(freq)
    #return(freq, lang)


def load_files(path):
    freqs=[]
    labels=[]
    file_list = glob.glob(path)
    #print(file_list)
    for fname in file_list:
        r=check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}

data=load_files("./lang/train/*.txt")
test=load_files("./lang/test/*.txt")

#json 형식으로 data와 test를 저장
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test],fp)

#학습하기
clf = svm.SVC()
clf.fit(data["reqs"],data["labels"])

#예측하기
predict = clf.predict(test["freqs"])

#결과 테스트하기
score = metrics.accuracy_score(test["labels"],predict)
report = metrics. classification_report(test["labels"],predict)
print("정답률=", score)
print("리포트=")
print(report)



# data="""
# kim 700101-1234567
# park 900202-2345678
# """
# result = []
# for line in data.split("\n"):
#     word_result = []
#     for word in line.split(" "):
#         #print(word)
#         if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
#             word=word[:6]+"-"+"*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))
# print("\n".join(result))


# import re
# data="""
# kim 700101-1234567
# park 900202-2345678
# """
# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******",data))


##############

# import re
# p = re.compile('[a-z]+')
# m = p.match("python")
# print(m)
# m2 = p.match("3 python")
# print(m2)
#
# """
# p=re.compile(정규표현식)
# m=p.match('문자열')
# if m:
#     print(매치됨, m.group())
# else:
#     print(매치안됨)
# """
#
# m3 = p.match("3 python")
# print(m3)
# result = p.findall("life is too short 3")
# print(result)
#
# result = p.finditer("life is too short")
# for r in result:
#     print(r)
#
# #어떤 문자열 매치되었을까? 매치된 문자열의 위치는 어디에서 어디까지인가
# #group(): 매치된 문자열 리턴, start/end(): 매치된 문자열 시작/끝 위치
# #span(): 매치된 문자열(시작,끝)에 해당하는 튜플을 리턴
# print("-------------------------------")
# m=p.match("python3")
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())
# print("-------------------------------")

# p = re.compile('[a-z]+')
# m=p.match("python")
# 위 구문을 축약해서 아래와 같이 표현 가능
# m=re.match('[a-z]+', "python")


############

import re
# p = re.compile('a.b')
# m=p.match('a\nb')
# print(m)  ##none

# p = re.compile('a.b', re.DOTALL)
# m=p.match('a\nb')
# print(m)

# p = re.compile('[a-z]', re.I)
# print(p.match('python'))
# print(p.match('Python'))
# print(p.match('PYTHON'))

# #|는 OR와 동일, A|B는 A또는 B를 의미
# p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)

# #ABC 문자열이 계속해서 반복되는지 조사하는 정규식을 작성하고 싶다면, 그룹핑을 사용하면 된다. 예를들어 (ABC)+
# p = re.compiel('(ABC)+')
# m = p.search()

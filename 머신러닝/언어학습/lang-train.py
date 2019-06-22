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


"""
정규표현식의 메타문자: 특별한 용도로 사용되는 문자 (. ^ $ * + ? {} [] () | 등)
1) 문자클래스 []
ex) 정규표현식 [abc] 의미? a,b,c 중에서 한 개의 문자와 매치
"a" : 정규식과 일치하는 문자인 "a"가 있으므로 매치됨
"before" : 정규식과 일치하는 문자인 "b"가 있으므로 매치됨
"dude" : 매치안됨

[]안에 두 문자 사이에 하이픈(-)을 사용하면 범위의 (from~to) 의미
[a-d]라는 표현식은 [abcd]와 같은 의미. [0-5]의미는 [012345]가 됨
[a-zA-Z] 알파벳 전체
[0-9] 숫자 전체
[^0-9] 숫자가 아닌 문자만 매칭


2) 정규표현식 별도 표기법
\d : 숫자와 매치, [0-9]와 같은 의미
\D : 숫자가 아닌것과 매치, [^0-9]와 같은 의미
\s : 공백문자(white space)와 매치 [ \t\n\r\f\v]과 같은 의미
\S : 공백문자(white space)가 아닌 것과 매치 [ ^\t\n\r\f\v]과 같은 의미
\w : 문자+숫자와 매치, [a-zA-Z0-9]와 같은 의미
\W : 문자+숫자가 아닌 것과 매치, [^a-zA-Z0-9]와 같은 의미

3) dot(.) : 줄바꿈 문자(\n)를 제외한 모든 문자와 매치됨을 의미
ex) 정규표현식이 a.b 라면,
"a+모든문자+b"와 같다
"aab"는 정규 식과 매치됨
"a0b"는 정규식과 매치됨
"abc"는 매치되지 않음, a와 b 사이에 적어도 하나의 문자가 있어야 하는데 없음
주의사항) [.]는 모든 문자가 아니며 단지 . 문자 그대로를 의미
a[.]b 정규식의 의미 : "a+dot(.)문자 +b"
a0b는 매치가 안됨

4) 반복(*)
ex) ca*t : *바로 아ㅠ에 있는 문자 a가 0부터 무한대까지 반복될 수 있음
문자열 ct는 매치됨. a가 0번 반복
cat은 매치됨. a가 1번 반복
caaaat는 매치됨

5) 반복(+) : 최소 한 번이상 반복될 때 사용
정규식 : ca+t 의미 a가 최소 1번 이상 나와야 함
ct는 매치안됨
cat은 매치됨. a가 1번 반복
caaaaat는 매치뒴

6)반복({m,n},?)
{m,n} 정규식은 반복횟구가 m부터 n까지 매칭될 수 있음
{3,} 반복횟구사 3번 이상, {,3} 반복횟수가 3번 이하
m을 생략하면 0과 동일, n을 생략하면 무한대와 같음
6-1) {m}
ca{2}t : c+a(2번 반복)+t
cat문자열 매치되지 않음
caat문자연 매치됨
6-2) {m,n}
ca{2,5}t : c+a(2-5번 반복)+t
cat 문자열은 매치되지 않음
caat 문자열은 매치됨
caaaaat 문자열은 매치됨

7) ? 의미는 {0,1]과 같음
ex) cb?c 라는 정규식은 a+b(있어도 되고 없어도 됨)+c
abc 문자열은 매치됨
ac 문자열은 매치됨

8) 파이썬은 정규표현식을 re모듈로 지원
import re
p=re.compile('ab*')
re.compile을 이용하여 정규표현식을 컴파일하고 컴파일된 패턴 객체를 이용해서 작업을 수행
컴파일된 패턴 객체를 이용해서 검색을 수행(4가지 매서드)
-match() : 문자열의 처음부터 정규식과 매치되는지 조사
-search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사
-findall() : 정규식과 매치되는 모든 문자열을 리스트로 리턴
-finditer() : 정규식과 매치되는 모든 문자열을 iterator로 리턴
"""

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


"""
9) 컴파일 옵션
DOTALL(S) - .(dot)이 줄바꿈 문자를 포함해서 매치할 수 있도록 해주는 옵션
IGNORECASE(I) - 대소문자 무시하고 매치할 수 있도록 해주는 옵션
MULTILINE(M) - 여러줄과 매치할 수 있도록 해주는 옵션
VERBOSE(X) - 정규식을 보기 쉽게 만들고, 주석을 사용할 수 있도록 해주는 옵션
*옵션 작성방법
re.DOTALL 형태로 쓰거나 re.S처럼 약자로 표기 가능
"""

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
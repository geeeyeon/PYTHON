from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("bmi.csv")
label = tbl["label"]
# print(label)
w = tbl["weight"] /100
h = tbl["height"] /200
wh = pd.concat([w,h], axis=1) # axis =1 열단위, axis =0 행단위

# 학습 데이터와 테스트 데이터 분리
data_train, data_test, label_train, label_test = train_test_split(wh, label)

# 학습하기
clf = svm.SVC()
clf.fit(data_train, label_train)
# 예측하기
predict = clf.predict(data_test)

# 결과 확인
score = metrics.accuracy_score(label_test, predict)
report = metrics.classification_report(label_test, predict)

print("정답률: ", score)
print("리포트: ", report)
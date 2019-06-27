import matplotlib.pyplot as plt
import pandas as pd

# x = [1,2,3,4,5]
# y = [1,4,9,16,25]
# fig = plt.figure()
# fig.add_subplot(1,1,1) # (2,2,2) 2x2 그리드의 2번째 위치에 출력
# plt.scatter(x,y)
# plt.show()

tbl = pd.read_csv("bmi.csv", index_col=2)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["weight"], b["height"], c=color, label = lbl)
scatter("fat", "red")
scatter("normal", "yellow")
scatter("thin", "purple")
ax.legend()
plt.savefig("bmi-test.png")
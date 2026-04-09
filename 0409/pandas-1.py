import pandas as pd

# 一維
p1 = pd.Series([20,30,50,80,60])
print(p1)
# 二維
p2 = pd.DataFrame(
    [
        [20,30,50,80,60],
        [21,32,53,84,65]
    ]
)
print(p2)
p3 = pd.DataFrame(
    {
        '姓名':['小名','小強','小美'],
        '分數':[90,85,88]
    }
)
print(p3)

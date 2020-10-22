import numpy as np

a = np.random.randint(1, 5, size=(5, 5))
assert (a.shape == (5, 5))  # 判断括号中的语句是否为真，否则终止程序
# print(np.dot(a, a.T))
sum = 0
for i in range(5):
    for j in range(5):
        if a[i][j] % 2 == 0:
            sum += a[i][j]
print(sum)
print(a)

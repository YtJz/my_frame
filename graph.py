import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec


def show1():
    fig = plt.figure(num=1, figsize=(4, 4))
    plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
    plt.show()


def show2():
    fig1 = plt.figure(num=1, figsize=(4, 4))
    ax = fig1.add_subplot(111)
    ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
    plt.show()


def show3():
    fig2 = plt.figure(num=1, figsize=(4, 4))
    ax1 = fig2.add_subplot(221)
    ax1.plot([1, 2, 3, 4], [1, 2, 3, 4])
    ax2 = fig2.add_subplot(222)
    ax2.plot([1, 2, 3, 4], [1, 1, 2, 3])
    ax3 = fig2.add_subplot(223)
    ax3.plot([1, 2, 3, 4], [1, 2, 2, 3])
    ax4 = fig2.add_subplot(224)
    ax4.plot([1, 2, 3, 4], [1, 2, 3, 3])
    plt.show()


def show4():
    fig3 = plt.figure(num=1, figsize=(4,6))
    gs = gridspec.GridSpec(3,3)
    ax1 = fig3.add_subplot(gs[-1, 2])
    ax1.plot([1, 2, 3, 4], [1, 2, 3, 3])
    plt.show()


#def show5():

apple = [78, 80, 79, 81, 91, 95, 96]
fig = plt.figure(num=1, figsize=(6, 4))  # 创建画布
x = np.arange(1, 8)  # 横坐标
ax = fig.add_subplot(221)  # 画布分块
ax.plot(x, apple)

# 图像的细节部分
ax.set_xlim([1, 7.1])  # 设置x的刻度从1到7.1
ax.set_ylim([40, 100])  # 设置y的刻度从40到100
ax.set_xticks(np.linspace(1, 7, 7))   # np.linspace()创建一个从1~7的7位等差数列
ax.set_yticks(np.linspace(50, 100, 6))  # 创建一个从50~100的6位等差数列

ax.set_xticklabels(["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"],
                   fontproperties="SimHei", fontsize=12, rotation=10)
ax.set_yticklabels(["50kg", "60kg", "70kg", "80kg", "90kg", "100kg"])

fig = plt.figure(num=1, figsize=(2, 2))
ax = fig.add_subplot(222)
x = np.arange(-100, 100)
y = (1-np.e**(-0.05*x))/(1+np.e**(-0.05*x))
ax.plot(x, y)


ax = fig.add_subplot(223)
x = np.arange(-100, 100)
y = (np.e**x-np.e**(-x))/(np.e**x+np.e**(-x))
ax.plot(x, y)

ax = fig.add_subplot(224)
x = np.arange(-10, 10, 0.01)
y = np.sin(x)
for n in range(3,10):
    if n%2!=0:
        y = y + (1/n)*np.sin(n*x)
x1 = np.arange(-6, 6)
ax.plot(x, y)
plt.show()

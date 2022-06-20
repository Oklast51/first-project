# Math Project
from numpy import *
from matplotlib import pyplot
from numpy.linalg import *
if __name__=='__main__':
    x1 = linspace(0, 60, 11)
    y1 = 100 - 2 * x1

    x2 = linspace(0, 60, 11)
    y2 = 50 - (3 * x2 / 4)

    x3 = linspace(0, 60, 11)
    y3 = 50 - (13 * x3 / 5)

    pyplot.xlim(-3, 62)
    pyplot.ylim(-3, 62)

    pyplot.plot(x1, y1, 'r', label='2x+y=100')
    pyplot.plot(x2, y2, 'g', label='3x+4y=200')
    pyplot.plot(x3, y3, 'b', label='13x+5y=250')
    pyplot.plot([0, 0], [0, 60])
    pyplot.plot([0, 60], [0, 0])

    # 解方程
    A = solve([[2, 1], [3, 4]], [100, 200])
    B = solve([[2, 1], [0, 1]], [100, 0])
    C = solve([[13, 5], [0, 1]], [250, 0])  # C=[19.23076923  0.]不是整數點，在後面計算時，根據其圖像手動取整
    D = solve([[3, 4], [1, 0]], [200, 0])  # D=[9.47390314e-15 5.00000000e+01]因為精度問題，輸出變成了float，實際上D=(0,50)
    # 代入目標函數求最大值
    k = array([48, 31])
    N = []
    for i in [A, B, c := [20, 0], D]:  # 因為要取整數，C調整為(20,0)
        N.append(k.dot(i))
    print(*N)
    print(max(N))

    # 輸出結果如下：
    # 2540.0000000000005 2400.0 923.0769230769231 1550.0000000000002
    # 2540.0000000000005
    # 用python作圖
    # 畫點
    pyplot.plot(A[0], A[1], "k.", markersize=10)
    pyplot.plot(B[0], B[1], "k.", markersize=10)
    pyplot.plot(C[0], C[1], "k.", markersize=10)
    pyplot.plot(D[0], D[1], "k.", markersize=10)
    # 插入點的符號
    pyplot.text(A[0], A[1] + 0.9, "A", fontsize=16, c='black')
    pyplot.text(B[0], B[1] + 0.9, "B", fontsize=16, c="black")
    pyplot.text(C[0], C[1] + 0.9, "C", fontsize=16, c="black")
    pyplot.text(D[0], D[1] + 0.9, "D", fontsize=16, c="black")
    pyplot.title("最大化客乘數量", fontfamily="simsun", fontsize=20)

    # 畫不等式解集
    x = []
    y = []
    for point in [A, B, C, D]:
        x.append(point[0])
        y.append(point[1])
    pyplot.fill(x, y, 'grey', alpha=0.3)

    # 座標標標籤
    pyplot.legend()
    pyplot.xlabel('大型巴士數量 x (輛)', fontfamily="simsun", fontsize=12, c='black')
    pyplot.ylabel('小型巴士數量 y (輛)', fontfamily="simsun", fontsize=12, c='black')
    pyplot.show()

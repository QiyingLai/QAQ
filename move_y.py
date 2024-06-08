import numpy as np


def move_y(f,delta_y):
    # 于对图像进行垂直方向移动
    #laiqiying 2024/6/6
    B = np.array([[1, 0, -1*delta_y],
                  [0, 1, 0],
                  [0, 0, 1]])
    m, n = f.shape
    g = np.zeros_like(f)
    for i in range(m):
        for j in range(n):
            temp = np.array([[i, j, 1]]).T
            temp = np.matmul(B, temp)
            y = temp[0][0]
            x = temp[1][0]
            if (y <= m) and (x <= n) and (x > 0) and (y > 0):
                g[y-1, x-1] = f[i, j]
    return g
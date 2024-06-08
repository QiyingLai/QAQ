import math

import numpy as np


def circle_fitting_v2(p):
    #此函数通过输入圆上的点的坐标来拟合圆方程，输出圆心坐标和半径
    #参考：https: // blog.csdn.net / jacky_ponder / article / details / 70314919
    m,n=p.shape
    p=p.astype(np.double)
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    x3 = 0
    y3 = 0
    x1y1 = 0
    x1y2 = 0
    x2y1 = 0

    for i in range(m):
        x1 = x1 + p[i, 0]
        y1 = y1 + p[i, 1]
        x2 = x2 + p[i, 0] * p[i, 0]
        y2 = y2 + p[i, 1] * p[i, 1]
        x3 = x3 + p[i, 0] * p[i, 0] * p[i, 0]
        y3 = y3 + p[i, 1] * p[i, 1] * p[i, 1]
        x1y1 = x1y1 + p[i, 0] * p[i, 1]
        x1y2 = x1y2 + p[i, 0] * p[i, 1] * p[i, 1]
        x2y1 = x2y1 + p[i, 0] * p[i, 0] * p[i, 1]
    N = m
    C = N * x2 - x1 * x1
    D = N * x1y1 - x1 * y1
    E = N * x3 + N * x1y2 - (x2 + y2) * x1
    G = N * y2 - y1 * y1
    H = N * x2y1 + N * y3 - (x2 + y2) * y1

    a = (H * D - E * G) / (C * G - D * D) #圆心坐标和半径
    b = (H * C - E * D) / (D * D - G * C)
    c = -(x2 + y2 + a * x1 + b * y1) / N
    y0 = -1 * a / 2
    x0 = -1 * b / 2
    R = math.sqrt(a * a + b * b - 4 * c) / 2;
    return x0,y0,R
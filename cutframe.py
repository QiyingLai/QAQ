import cv2
import numpy as np


def cutframe(f, x1, x2, y1, y2):
    # 用于除去原图旋转平移后胶片以外的区域
    # 输入：x1,x2,y1,y2    胶片左上和右上两个顶点的坐标
    # laiqiying 2024/6/6
    m, n = f.shape
    tmp = np.zeros_like(f)
    x0=round((n-x2)*0.30)
    y0=round(y1*0.30)
    x2=x2-x0
    y1=y1+y0
    i = round(y1*1.3)
    x1=x1+x0
    y2 = y2-y0
    while i < y2:
        j = x1 - 1
        while j < x2:
            tmp[i][j] = 1
            j += 1
        i += 1
    tmp = np.multiply(f, tmp)
    return tmp
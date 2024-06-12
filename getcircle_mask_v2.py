import numpy as np


def getcircle_mask_v2(f,y0,x0,r):
    #laiqiying 2024/6/8
    m,n=f.shape
    x0=round(x0)
    y0=round(y0)
    m1=range(-x0-1,m-x0-1)
    n1=range(-y0-1,n-y0-1)
    x, y = np.meshgrid(n1, m1)
    circle = np.multiply(x,x)+np.multiply(y,y)#计算出每一点到圆心的距离的平方
    circ_mask=np.zeros_like(f)
    r0=0.9*r#取半径以内的点
    R2=r0*r0
    circ_mask[circle<=R2]=1#找到圆内的元素，并复制为1
    return circ_mask
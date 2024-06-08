import cv2
import numpy as np
from getline_v2 import getline_v2
from getpara import getpara


def image_rotation_angle(g):
    #得到图像旋转角度
    #最小二乘法确定直线斜率和截矩，只适用于不垂直于x轴直线
    #laiqiying 2024/6/5
    bottom = getline_v2(g, 'bottom')
    x,y=getpara(bottom)
    if len(x)<20:
        top=getline_v2(g,'top')
        x,y=getpara(top)

    k=0
    b=0
    x=np.array(x)
    y=np.array(y)
    if len(x)>10:
        k,b = np.polyfit(x, y, 1)
    return k,b
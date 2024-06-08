import cv2
import numpy as np

from cut import cut
from filter_v2 import filter_v2
from getline_v2 import getline_v2
from getpara import getpara
from image_rotation_angle import image_rotation_angle
from move_x import move_x
from move_y import move_y
from myreverse import myreverse
from scipy.ndimage import rotate

from myreverse_back import myreverse_back
from tobw import tobw


def line_operation(f,ori):
    #用于旋转平移原图，使其与原点对齐
    # p: 进行旋转的基准直线坐标
    # f: 基准二值图，用于提供旋转角度和平移量
    # ori: 灰度图，原图
    #如果图像边界像素值变化太小，无法识别边界，此种情况下使用enlarge值
    #laiqiying 2024/6/6
    k,b=image_rotation_angle(f)#k:直线斜率，b:截距
    ori=myreverse(ori)#先取反，再旋转，再取反，可以防止灰度图在第二次二值化的时候出现黑边

    theta=np.arctan(k)
    angle=180*theta/np.pi

    g = rotate(f, angle, reshape=False, order=3, mode='constant', cval=0)
    ori = rotate(ori, angle, reshape=False, order=3, mode='constant', cval=0)
    M,N=ori.shape
    ori = myreverse_back(ori)

    bw = tobw(ori)#旋转后的图二值化
    c = filter_v2(bw)
    left = getline_v2(c, 'left')
    bottom = getline_v2(c, 'bottom')
    x_l,y_l = getpara(left)
    x_b,y_b = getpara(bottom)

    x_l=np.array(x_l)
    y_l = np.array(y_l)
    x_b = np.array(x_b)
    y_b = np.array(y_b)
    size_left = len(x_l)
    size_bottom = len(x_b)
    x0=0
    y0=0
    if size_left>0:#部分图像边界像素值过度太小，无法识别边界，此种情况下修回为enlarge值，下同
        for x in x_l:
            x0=x0+x
        x0=round(x0/size_left)#旋转后左边框的横坐标取平均，确定水平平移量,左边界
    else:
        x0=round(N*0.06)
    if size_bottom>0:
        for y in y_b:
            y0=y0+y
        y0 = round(y0 / size_bottom)
        y0 = M - y0#旋转后下边框的横坐标取平均，确定垂直平移量，下边界 ?
    else:
        y0 = round(0.06 * M)#?

    ori = myreverse(ori) #取反
    result = move_x(ori, x0) #平移
    result = move_y(result, -y0)
    result = myreverse_back(result)

    bw2 = tobw(result);
    c2 = filter_v2(bw2);
    top = getline_v2(c2, 'top')
    right = getline_v2(c2, 'right')

    x_t,y_t = getpara(top)
    x_r,y_r = getpara(right)
    size_top = len(x_t)
    size_right = len(x_r)
    x1=0
    y1=0

    if size_top>0:
        for y in y_t:
            y1=y1+y
        y1=round(y1/size_top)
    else:
        y1=round(M*0.06)

    if size_right>0:
        for x in x_r:
            x1=x1+x
        x1=round(x1/size_right)
    else:
        x1=round(0.88*N)
    result = cut(result, 1, x1, y1, M)
    r=np.array([x0,y0,angle])
    return r, result, x1, y1

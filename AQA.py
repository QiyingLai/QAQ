import cv2
import numpy as np
from scipy.signal import find_peaks

def AQA(f):
    #灰度图转二值图
    gf=cv2.blur(f,(5,5),borderType=cv2.BORDER_REPLICATE)#5*5均值滤波器

    #直方图可以用来评价一个图形的各个像素分布
    hist = cv2.calcHist([gf], [0], None, [256], [0, 255])
    # hist=hist.astype(np.).T
    hist=hist.T
    h=np.squeeze(hist,axis=0)#得到一个一维数组，表示0~255的256个值出现的次数

    peaks, _ = find_peaks(h, height=400, distance=10)#最小峰值高度400，最小峰值间隔10。得到符合条件的峰值对应于输入的索引。
    pk_max=0
    for i in peaks:#找到所有峰值的最大值
        if h[i]>pk_max:
            pk_max=h[i]
    delta_pk = pk_max / 4#峰值的四分之一
    peaks, _ = find_peaks(h, height=delta_pk, distance=10)#重新寻找峰值，即峰值的位置
    delta=peaks[0]/255+0.04
    delta=delta*255#峰值的第一个位置除以255+0.04获得比例，然后乘上255，作为二值化的阈值
    _,g = cv2.threshold(gf, delta, 255, cv2.THRESH_BINARY)

    g = cv2.blur(g, (9, 9), borderType=cv2.BORDER_REPLICATE)#均值滤波

    g = cv2.GaussianBlur(g, (11, 11), 2.55)
    G = cv2.Canny(g, threshold1=10, threshold2=70, L2gradient=True)#边缘检测
    return G
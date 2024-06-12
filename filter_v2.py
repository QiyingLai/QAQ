import cv2
import numpy as np
from skimage import morphology

def filter_v2(f):
    #对二值图像依次做边缘检测 / 膨胀 / 中值滤波 / 均值滤波 / 连通面积检测 / 细化处理 / 均值滤波
    #用于得到平滑的胶片边框
    #laiqiying 2024/6/4
    f = cv2.GaussianBlur(f, (11,11), 0)
    g=cv2.Canny(f,threshold1=10,threshold2=70,L2gradient=True,apertureSize=3)

    g=cv2.dilate(g,np.ones((4, 4), np.uint8))

    g = cv2.medianBlur(g, 5)

    g=cv2.blur(g,(5,5),borderType=cv2.BORDER_REPLICATE)
    n, L, stats, _ = cv2.connectedComponentsWithStats(g, connectivity=8)
    g = np.zeros_like(g)
    for (i, label) in enumerate(np.unique(L)):
        # 如果是背景，忽略
        if label == 0:
            continue
        if stats[i][-1] >= 100:
            g[L == i] = 255
    #细化
    # skel, distance = morphology.medial_axis(g, return_distance=True)
    # g = distance * skel
    g = morphology.skeletonize(g)
    g = g.astype(np.uint8) * 255
    g = cv2.blur(g, (3, 3), borderType=cv2.BORDER_REPLICATE)
    g[g >0] = 255
    return g
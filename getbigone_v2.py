import cv2
import numpy as np

from cutframe import cutframe


def getbigone_v2(f,x1,y1):
    M,N=f.shape
    f=cutframe(f, 1, x1, y1, M)#去掉框

    t=300
    n1, L1, stats1, _ = cv2.connectedComponentsWithStats(f, connectivity=8)#连通区域检测
    f1 = np.zeros_like(f)
    f2 = np.zeros_like(f)
    g=np.zeros_like(f)
    max_stat_size=0
    max_stat_index=0

    for (i, label) in enumerate(np.unique(L1)):
        if label != 0 and max_stat_size<stats1[i][-1]:#寻找除了背景外，最大的连通区域，假设最大连通区是大圆
            max_stat_index=i
            max_stat_size=stats1[i][-1]
        if label == 0:
            continue
        if stats1[i][-1] >= t:#去除字母，两个圆
            f1[L1 == i] = 255

    if max_stat_index==0:
        return None
    f2[L1==max_stat_index]=255#只有大圆的图
    return f2,f1
import cv2
import numpy as np


def getbigone(f):
    #抠出大圆
    #laiqiying 2024/6/6
    t=300
    n1, L1, stats1, _ = cv2.connectedComponentsWithStats(f, connectivity=8)#连通区域检测
    f1 = np.zeros_like(f)
    f2 = np.zeros_like(f)
    g=np.zeros_like(f)
    max_stat_size=0
    max_stat_index=0

    for (i, label) in enumerate(np.unique(L1)):
        if label != 0 and max_stat_size<stats1[i][-1]:#寻找除了背景外，最大的连通区域，假设最大连通区是框
            max_stat_index=i
            max_stat_size=stats1[i][-1]
        if label == 0:
            continue
        if stats1[i][-1] >= t:#去除字母，获取框和两个圆
            f1[L1 == i] = 255
    if max_stat_index==0:
        return None
    f2[L1==max_stat_index]=255#只有框的图
    f3 = np.bitwise_xor(f1, f2)#去掉框

    n2, L2, stats2, _ = cv2.connectedComponentsWithStats(f3, connectivity=8)
    max_stat_size=0
    max_stat_index=0
    for (i, label) in enumerate(np.unique(L2)):
        if label != 0 and max_stat_size<stats2[i][-1]:
            max_stat_index=i
            max_stat_size=stats2[i][-1]
    g[L2==max_stat_index]=255#取最大圆
    return g,f3




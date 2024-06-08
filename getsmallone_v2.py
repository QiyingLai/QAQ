import cv2
import numpy as np


def getsmallone_v2(f):
    g=np.zeros_like(f)
    n2, L2, stats2, _ = cv2.connectedComponentsWithStats(f, connectivity=8)
    max_stat_size = 0
    max_stat_index = 0
    for (i, label) in enumerate(np.unique(L2)):
        if label != 0 and max_stat_size < stats2[i][-1]:
            max_stat_index = i
            max_stat_size = stats2[i][-1]
    g[L2 == max_stat_index] = 255  # 取最大圆
    g=np.bitwise_xor(g, f)
    return g
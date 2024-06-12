import cv2
import numpy as np
from skimage import morphology


def filter_v3(f):
    # 对二值图像依次做边缘检测 / 膨胀 / 中值滤波 / 均值滤波 / 连通面积检测 / 细化处理 / 均值滤波
    # 用于得到平滑的胶片边框
    # laiqiying 2024/6/4
    # f = cv2.GaussianBlur(f, (11, 11), 0)
    scharrx = cv2.Scharr(f, cv2.CV_32F, 1, 0)

    # 应用Scharr算子检测垂直边缘
    scharry = cv2.Scharr(f, cv2.CV_32F, 0, 1)

    # 计算边缘强度
    edges = cv2.magnitude(scharrx, scharry)

    # 转换为8位图像
    g = cv2.convertScaleAbs(edges)
    g = cv2.dilate(g, np.ones((4, 4), np.uint8))

    g = cv2.medianBlur(g, 5)

    g = cv2.blur(g, (5, 5), borderType=cv2.BORDER_REPLICATE)
    n, L, stats, _ = cv2.connectedComponentsWithStats(g, connectivity=8)
    g = np.zeros_like(g)
    for (i, label) in enumerate(np.unique(L)):
        # 如果是背景，忽略
        if label == 0:
            continue
        if stats[i][-1] >= 100:
            g[L == i] = 255
    # 细化
    # skel, distance = morphology.medial_axis(g, return_distance=True)
    # g = distance * skel
    g = morphology.skeletonize(g)
    g = g.astype(np.uint8) * 255
    g = cv2.blur(g, (3, 3), borderType=cv2.BORDER_REPLICATE)
    g[g > 0] = 255
    return g
    # cv2.imshow('Edges', g)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
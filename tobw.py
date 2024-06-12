import cv2


def tobw(f):
    #得到二值化图片,大津法确定阈值
    #laiqiying 2024/6/4
    T,G=cv2.threshold(f,0,255,cv2.THRESH_OTSU)
    # cv2.adaptiveThreshold()
    #cv2.minEnclosingCircle()

    return G
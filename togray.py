import cv2
def togray(f):
    # 输入RGB图像
    # 按照Gray = R * 0.299 + G * 0.587 + B * 0.114
    # 进行灰度转换
    # 输出灰度图像
    #laiqiying 2024/6/3
    g=f
    dimension=f.ndim
    if dimension==3:
        g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    return g


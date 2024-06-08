from togray import togray
import numpy as np
def enlarge(f):
    # 扩展图像边缘，直接赋值,图像四个边缘方向各扩大5%
    f_grey=togray(f)
    m,n=f_grey.shape
    row=np.zeros((round(0.05*m),n))
    row[:,:]=255
    g=np.pad(f_grey,pad_width=(round(0.05*m),round(0.05*n)),mode='constant',constant_values=255)
    return g
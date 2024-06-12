import cv2
import numpy as np
from PIL import Image
from Main import Main

# fileName_LS = r'D:\QAQ\AQA_HuJY\data\20170601A.tif'
# fileName_AS = r'D:\QAQ\AQA_HuJY\data\20170601B.tif'

# fileName_LS = r'D:\QAQ\AQA_HuJY\data\20140414A.tif'
# fileName_AS = r'D:\QAQ\AQA_HuJY\data\20140414B.tif'

# fileName_LS = r'D:\QAQ\AQA_HuJY\data\20150128A.tif'
# fileName_AS = r'D:\QAQ\AQA_HuJY\data\20150128B.tif'

fileName_LS = r'D:\QAQ\AQA_HuJY\data\20170629A.tif'
fileName_AS = r'D:\QAQ\AQA_HuJY\data\20170629B.tif'

#cv2读取的图像数据类型默认是8位无符号整数
AS=cv2.imread(fileName_AS)
LS=cv2.imread(fileName_LS)
#获取水平和垂直dpi
info_AS=Image.open(fileName_AS)
info_LS=Image.open(fileName_LS)
XResolution_AS, YResolution_AS=info_AS.info.get('dpi')
XResolution_LS, YResolution_LS=info_AS.info.get('dpi')
# Main(AS)
ori_g_AS,ori_r_AS,circle_small_AS,circle_big_AS,x1_AS,y1_AS,d_AS,m_AS,x_offset_AS,y_offset_AS=Main(AS)
ori_g_LS,ori_r_LS,circle_small_LS,circle_big_LS,x1_LS,y1_LS,d_LS,m_LS,x_offset_LS,y_offset_LS=Main (LS)

x_offset_AS = x_offset_AS*25.4/XResolution_AS
y_offset_AS = y_offset_AS*25.4/YResolution_AS
x_offset_LS = x_offset_LS*25.4/XResolution_LS
y_offset_LS = y_offset_LS*25.4/YResolution_LS

SI=(y_offset_AS+y_offset_LS)/2
LR = x_offset_LS
AP = x_offset_AS

TOTAL = np.sqrt(SI**2+LR**2+AP**2)

print(TOTAL)


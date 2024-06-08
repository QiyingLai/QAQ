import cv2
import numpy as np


def getline_v2(f,location):
    #此函数用来得到胶片四条边的图像
    #修改取边框的条件，去除中间圆圈的干扰
    #laiqiying 2023/6/5
    m,n=f.shape
    temp = np.zeros_like(f)
    if location=='left':
        i_start=round(m*0.3)
        i_end=round(m*0.7)
        j_start=0
        j_end=round(n*0.15)
        while i_start<i_end:
            j=j_start
            while j<j_end:#只考虑0~0.15之间区域，在此区域内没有投影圆
                if(f[i_start,j]==255):
                    temp[i_start,j]=255
                j+=1
            i_start+=1
        s=np.sum(temp,axis=1)
        for t in range(m):
            if s[t]>5*255:
                temp[t,:]=0 #将左边框上检测到的点的数量逐行求和，若数量过大，则弃用这些点，下同
        return temp
    elif location=='right':
        i_start=round(m*0.3)
        i_end=round(m*0.7)
        j_start=round(n*0.85)
        j_end=n
        while i_start<i_end:
            j = j_start
            while j<j_end:#只考虑0.85~1之间区域，在此区域内没有投影圆
                if(f[i_start,j]==255):
                    temp[i_start,j]=255
                j+=1
            i_start+=1
        s=np.sum(temp,axis=1)
        for t in range(m):
            if s[t]>5*255:
                temp[t,:]=0
        return temp
    elif location=='top':
        i_start = 0
        i_end = round(m * 0.15)
        j_start = round(n * 0.3)
        j_end = round(n * 0.7)
        while j_start < j_end:
            i=i_start
            while i < i_end:
                if (f[i, j_start] == 255):
                    temp[i, j_start] = 255
                i += 1
            j_start += 1
        s = np.sum(temp, axis=0)
        for t in range(n):
            if s[t] > 5*255:
                temp[:, t] = 0
        return temp
    elif location=='bottom':
        i_start = round(m * 0.85)
        i_end = m
        j_start = round(n * 0.3)
        j_end = round(n * 0.7)
        num=0
        while j_start < j_end:
            i=i_start
            while i < i_end:
                num+=1
                if (f[i][j_start] == 255):
                    temp[i][ j_start] = 255
                i += 1
            j_start += 1
        s = np.sum(temp, axis=0)
        for t in range(n):
            if s[t] > 5*255:
                print(s[t])
                temp[:, t] = 0
        return temp






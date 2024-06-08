def getpara(f):
    #用于得到getline_v2函数输出图像上直线的坐标值
    m,n=f.shape
    k=0
    x=[]
    y=[]

    for i in range(m):
        for j in range(n):
            if f[i][j]==255 :
                x.append(j)
                y.append(i)
    return x,y


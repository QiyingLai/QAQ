
def myreverse(f):
    #用于对图像进行灰度取反
    #laiqiying 2024/6/5
    m,n=f.shape
    for i in range(m):
        for j in range(n):
            f[i][j]=255-f[i][j]
    return f

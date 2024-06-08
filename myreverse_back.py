def  myreverse_back(f):
    #用于对图像进行灰度取反
    #laiqiying 2024/6/6
    M,N=f.shape
    for i in range(M):
        for j in range(N):
            f[i][j]=255-f[i][j]
    return f
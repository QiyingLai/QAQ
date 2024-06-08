import numpy as np


def getpoint(f):
    m,n=f.shape
    p=[]
    for i in range(m):
        for j in range(n):
            if f[i][j]==255:
                p.append([i,j])
    p=np.array(p)
    return p

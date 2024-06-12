import numpy as np

from getcircle_mask_v2 import getcircle_mask_v2


def getsmallone_v3(f,x,y,r):
    circle_mask = getcircle_mask_v2(f, x, y, r)
    g=np.multiply(f,circle_mask)
    return g
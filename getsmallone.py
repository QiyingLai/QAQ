import cv2
import numpy as np

from getcircle_mask import getcircle_mask


def getsmallone(f,x,y,r):
    circle_mask = getcircle_mask(f, x, y, r)
    g=np.multiply(f,circle_mask)

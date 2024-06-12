import cv2
import numpy as np

from AQA import AQA
from circle_fitting_v2 import circle_fitting_v2
from enlarge import enlarge
from filter_v2 import filter_v2
from filter_v3 import filter_v3
from getbigone import getbigone
from getbigone_v2 import getbigone_v2
from getpoint import getpoint
from getsmallone_v2 import getsmallone_v2
from getsmallone_v3 import getsmallone_v3
from line_operation import line_operation
from tobw import tobw


def Main(f):
    ori_gray=enlarge(f)
    ori_bw=tobw(ori_gray)
    # ori_bw=filter_v3(ori_bw)
    ori_bw=filter_v2(ori_bw)
    ori_r,ori_f,x1,y1=line_operation(ori_bw,ori_gray)
    ori_g = AQA(ori_f)
    m,n=ori_g.shape
    big,big_and_small=getbigone_v2(ori_g,x1,y1)
    # big,big_and_small = getbigone(ori_g)

    p_big = getpoint(big)
    x0,y0,R = circle_fitting_v2(p_big)

    # small = getsmallone_v2(big_and_small)
    small = getsmallone_v3(big_and_small, x0, y0, R)
    p_small = getpoint(small)
    x_s,y_s,R_s = circle_fitting_v2(p_small)
    x_b=x0
    y_b=y0

    x_offset = x_b - x_s
    y_offset = y_b - y_s
    d = np.sqrt((x_b - x_s) ** 2 + (y_b - y_s) ** 2)
    circle_big=np.array([x0,y0,R])
    circle_small=np.array([x_s,y_s,R_s])

    return ori_g, ori_r, circle_small, circle_big, x1, y1, d, m, x_offset, y_offset
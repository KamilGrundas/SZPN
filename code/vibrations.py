import math
from settings import *


def damped_vibrations(start_y, t, k, m, n):
    w_0 = math.sqrt(k / m)

    b = n / (2 * m)

    try:
        w = math.sqrt((w_0**2) - (b / (2 * m)) ** 2)
    except:
        w = 0
    if w_0 == 0:
        y = start_y
    else:
        y = start_y * math.exp((-b / (2 * m)) * t) * math.cos(w * t)

    return y


def damped_vibrations_max(k, m, n):
    w_0 = math.sqrt(k / m)
    b = n / (2 * m)
    bk = 2 * w_0 * m
    return [b, bk]


def forced_vibrations(w, t):
    y = 0.5 * math.cos(w * t)
    return y

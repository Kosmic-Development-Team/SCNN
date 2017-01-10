import Image
from convolution import kernels
from convolution import warpfuncs
import math


def convolute(k, li, w, h):  # k and l are the pixel components
    sd = (w - kernels.fulldim[0] + 1, h - kernels.fulldim[1] + 1)
    nli = Image.new('RGB', sd)
    newl = nli.load()
    __stretch(__convkern(newl, k, li, w, h), newl, sd[0], sd[1], k.wrp)
    return nli


def __stretch(mnmx, newl, w, h, f):
    tran = mnmx[0]
    mult = (255 / (mnmx[1] - tran)) + 0.00001  # 0.00001 to prevent top value going to 254
    for i in range(w):
        for j in range(h):
            fix = math.floor((newl[i, j][0] - tran) * mult)
            if f is not 0:
                fix = int(warpfuncs.warpfuncs[f - 1](fix))
            newl[i, j] = (fix, fix, fix)


def __convkern(newl, k, li, w, h):
    mx = 0
    mn = 255
    for i in range(h - (kernels.dim[1] * 2)):
        for j in range(w - (kernels.dim[0] * 2)):
            te = 0
            for m in range(kernels.fulldim[0]):
                for n in range(kernels.fulldim[1]):
                    te += li[j + n, i + m][0] * k.kern[kernels.fulldim[0] - m - 1][kernels.fulldim[1] - n - 1]
            ave = 255 - int((te / k.div) + k.add)
            mx = max(mx, ave)
            mn = min(mn, ave)
            newl[j, i] = (ave, ave, ave)
    return mn, mx

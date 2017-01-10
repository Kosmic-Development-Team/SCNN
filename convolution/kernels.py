import Image


dim = (2, 2)  # border not including mid pixel or opposite side
fulldim = ((dim[0] * 2) + 1, (dim[1] * 2) + 1)
area = fulldim[0] * fulldim[1]
kernels = []
name = 'k'
foldername = 'kernels/'
path = 'C:/Users/Kosmic/Documents/PythonProjects/SCNN/'


def loadkernel(num):
    kern = open(path + foldername + name + str(num) + '.kern').read()
    us = kern.split('\n')
    uns = []
    for u in us:
        uu = u.split(' ')
        while True:
            try:
                uu.remove('')
            except:
                break
        uns += uu

    k = []
    for i in range(fulldim[0]):
        k.append([])
        for j in range(fulldim[1]):
            k[i].append(int(uns[i * fulldim[0] + j]))
    kernels.append(Kernel(k, int(uns[area]), int(uns[area + 1]), int(uns[area + 2])))


class Kernel:
    def __init__(self, k, d, a, w):
        self.kern = k
        self.div = d
        self.add = a
        self.wrp = w

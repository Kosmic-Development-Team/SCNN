import Image
from convolution import convolute
from convolution import kernels

kernels.loadkernel(2)
im = Image.open('C:/Users/Kosmic/Documents/PythonProjects/SCNN/test.png')
w, h = im.size
l = convolute.convolute(kernels.kernels[0], im.load(), w, h)
for i in range(0):
    l = convolute.convolute(kernels.kernels[0], l.load(), w - (4 * (i + 1)), h - (4 * (i + 1)))
l.show()

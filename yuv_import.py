import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def yuv_import(filename, dims, numfrm, startfrm):
    fp = open(filename, 'rb')
    blk_size = np.prod(dims) * 3 / 2
    fp.seek(np.int(blk_size * startfrm), 0)

    d00 = dims[0] // 2
    d01 = dims[1] // 2

    Y = np.zeros((numfrm, dims[0], dims[1]), np.uint8, 'C')
    U = np.zeros((numfrm, d00, d01), np.uint8, 'C')
    V = np.zeros((numfrm, d00, d01), np.uint8, 'C')

    for i in range(numfrm):
        for m in range(dims[0]):
            for n in range(dims[1]):
                # print m,n
                Y[i, m, n] = ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                U[i, m, n] = ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                V[i, m, n] = ord(fp.read(1))
    fp.close()
    return (Y, U, V)

def main(argv=None):  # pylint: disable=unused-argument
   Y,U,V = yuv_import("./BasketballPass_raw.yuv", (240, 416), 100, 0)
   y1 = Y[0]
   y2 = Y[10]

   plt.imshow(y1,cmap='gray' )
   plt.imshow(y2,cmap='gray')
   plt.show()



if __name__ == '__main__':
    main()

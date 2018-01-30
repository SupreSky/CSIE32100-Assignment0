import cv2
import time
import numpy as np

## Read Files
img = cv2.imread("../Assignment3/images/i1.pgm", 0)
img2 = cv2.imread("../Assignment3/images/i2.pgm", 0)
img3 = np.copy(img)
img4 = np.copy(img)

## Calc MAD in seq_search()
def MAD_1(x, y, i, j):
    dSum = 0
    for k in range(i-8, i+8):
        for l in range(j-8, j+8):
            C = img2[x+k-i,y+l-j]
            R = img[k, l]
            dSum = dSum + abs(C-R)
    return dSum

## Calc MAD in twoD_search()
def MAD_2(R, C):
    cAns = 0
    minAns = 1e9
    for i in range(0, 3):
        for j in range(0, 3):
            cAns = abs(C[i][j]-R[i][j])
            if cAns < minAns:
                minAns = cAns
                u = i
                v = j
    u = u - 1
    v = v - 1
    return u, v

## Calc SNR
def SNR(f1, f2):
    Up = 0
    Down = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            A = int (f1[x, y])
            B = int (f2[x, y])
            print ( Up, Down )
            Up = Up + (B ** 2)
            Down = Down + ( ( A - B ) ** 2 )
    
    ans = Up / Down
    return ans


def seq_search():
    for x in range(8, img.shape[0], 16):
        for y in range(8, img.shape[1], 16):
            minMAD = 1e9
            """ Calc MAD in window """
            for i in range(x-15, x+16):
                if i < 0 or i+7 >= img.shape[0]:
                    continue
                for j in range(y-15, y+16):                    
                    if j < 0 or j+7 >= img.shape[1]:
                        continue
                    curMAD = MAD_1(x, y, i, j)
                    """ If MAD is smaller than store it """
                    if curMAD < minMAD:
                        minMAD = curMAD
                        u = i
                        v = j
            """ Write predicted frames to file """
            for a in range(u-8, u+8):
                for b in range(v-8, v+8):
                    img3[x+a-u, y+b-v] = img[a,b]
                    

def twoD_search():
    for x in range(7, img.shape[0], 16):
        for y in range(7, img.shape[1], 16):
            flag = False
            oSet = 8
            """ Store 9 pixel in 3x3 array for the 9 searching direction"""
            nine = np.zeros((3,3))
            nine2 = np.zeros((3,3))
            k = x
            l = y
            while flag == False:
                nine = img[[k-oSet, k, k+oSet], :][:, [l-oSet, l, l+oSet]]
                nine2 = img2[[k-oSet, k, k+oSet], :][:, [l-oSet, l, l+oSet]]
                """ Calc MAD for the 9 Direction """
                u, v = MAD_2(nine, nine2)
                if oSet == 1:
                    flag = True
                oSet = int(oSet / 2)
                k = k + (u * oSet)
                l = l + (v * oSet)
                
            """ Write predicted frames to file """
            for a in range(k-8, k+8):
                for b in range(l-8, l+8):
                    if a >= img.shape[0] or b >= img.shape[1]:
                        continue
                    img4[x+a-k, y+b-l] = img[a, b]
                              
## Calc seq_search time and SNR
timeStart = time.time()
seq_search()
timeEnd = time.time()
seq_snr = SNR(img3, img)
print("Seq Time: ")
print(timeEnd-timeStart)
print("Seq SNR: ")
print(seq_snr)
         
## Calc twoD_search time and SNR
timeStart = time.time()
twoD_search()
timeEnd = time.time()
#twoD_snr = SNR(img4, img)
print("2D Time: ")
print(timeEnd-timeStart)
print("2D SNR: ")
print(twoD_snr)

cv2.imwrite("../Assignment3/images/i2p_Seq.pgm", img3)
cv2.imwrite("../Assignment3/images/i2p_2D.pgm", img4)
                
#cv2.imshow('image1',img)
#cv2.imshow('image2',img2)
cv2.imshow('image3',img3)
cv2.imshow('image4',img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
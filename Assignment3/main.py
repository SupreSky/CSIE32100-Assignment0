import cv2
import time
import numpy as np



P = 31

img = cv2.imread("../Assignment3/images/i1.pgm", 0)
img2 = cv2.imread("../Assignment3/images/i2.pgm", 0)
img3 = img


def MAD(x, y, i, j):
    dSum = 0
#    cK = -8
#    cL = -8
    for k in range(i-8, i+8):
        for l in range(j-8, j+8):
#            if x == 8 and y == 312 and i == 0 and j == 313:
#                print(x, y, i, j, k, l)
            C = img2[x+k-i,y+l-j]
            R = img[k, l]
            dSum = dSum + abs(C-R)
    return dSum
    
            

def seq_search():
    for x in range(8, img.shape[0], 16):
        for y in range(8, img.shape[1], 16):
            minMAD = 1e9
            for i in range(x-15, x+16):
                if i < 0 or i+7 >= img.shape[0]:
                    continue
                for j in range(y-15, y+16):
                    
                    
                    if j < 0 or j+7 >= img.shape[1]:
                        continue
                    curMAD = MAD(x, y, i, j)
                    if curMAD < minMAD:
                        minMAD = curMAD
                        u = i
                        v = j
            
#            for a, cA in zip(range(u-8, u+8), range(-8, 7)):
#                for b, cB in zip(range(v-8, v+8), range(-8, 7)):
            for a in range(u-8, u+8):
                for b in range(v-8, v+8):
                    img3[x+a-u, y+b-v] = img[a,b]
            
#            print(x*100/img.shape[0], y*100/img.shape[1])
                    
timeStart = time.time()
seq_search()
timeEnd = time.time()
print("Time: ")
print(timeEnd-timeStart)
                    
print(img3)

cv2.imwrite("/images/i2p.pgm", img3)
                

#cv2.imshow('image1',img)
#cv2.imshow('image2',img2)
cv2.imshow('image3',img3)
#cv2.imshow('image3',cv2.absdiff(img, img2))
cv2.waitKey(0)
cv2.destroyAllWindows()
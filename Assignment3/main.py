import cv2
import time
import numpy as np



P = 31

img = cv2.imread("../Assignment3/images/i1.pgm", 0)
img2 = cv2.imread("../Assignment3/images/i2.pgm", 0)
img3 = img


def MAD_1(x, y, i, j):
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

def MAD_2(R, C):
    cSum = 0
    minSum = 1e9
    for i in range(0, 9):
        cSum = cSum + abs(C[i]-R[i])
        if cSum < minSum:
            minSum = cSum
    return minSum
    
            

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
                    curMAD = MAD_1(x, y, i, j)
                    if curMAD < minMAD:
                        minMAD = curMAD
                        u = i
                        v = j
            
#            for a, cA in zip(range(u-8, u+8), range(-8, 7)):
#                for b, cB in zip(range(v-8, v+8), range(-8, 7)):
            for a in range(u-8, u+8):
                for b in range(v-8, v+8):
                    img3[x+a-u, y+b-v] = img[a,b]

def twoD_search():
    for x in range(7, img.shape[0], 16):
        for y in range(7, img.shape[1], 16):
            flag = False
            oSet = 8
            nine = np.zeros(9)
            nine2 = np.zeros(9)
            print(x+oSet, y+oSet)
            nine[0] = img[x-oSet, y-oSet]
            nine[1] = img[x, y-oSet]
            nine[2] = img[x+oSet, y-oSet]
            nine[3] = img[x-oSet, y]
            nine[4] = img[x, y]
            nine[5] = img[x+oSet, y]
            nine[6] = img[x-oSet, y+oSet]
            nine[7] = img[x, y+oSet]
            nine[8] = img[x+oSet, y+oSet]
            
            nine2[0] = img2[x-oSet, y-oSet]
            nine2[1] = img2[x, y-oSet]
            nine2[2] = img2[x+oSet, y-oSet]
            nine2[3] = img2[x-oSet, y]
            nine2[4] = img2[x, y]
            nine2[5] = img2[x+oSet, y]
            nine2[6] = img2[x-oSet, y+oSet]
            nine2[7] = img2[x, y+oSet]
            nine2[8] = img2[x+oSet, y+oSet]
            
            while flag == False:
                minSum = MAD_2(nine, nine2)
                if oSet == 1:
                    flag = True
                oSet = oSet / 2
                
                
                
                    
timeStart = time.time()
#seq_search()
twoD_search()
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
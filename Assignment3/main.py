import numpy as np
import cv2


P = 31
img = cv2.imread("../Assignment3/images/i1.pgm", 0)
img2 = cv2.imread("../Assignment3/images/i2.pgm", 0)


def MAD(x, y, i, j):
    dSum = np.zeros
    for k in range(16):
        for l in range(16):
            C = img[x:x+k, y:y+l]
            R = img[x+i:x+i+k, y+j:y+j+l]
            dSum = dSum + np.absolute(C-R)
    ans = dSum / 256
    return ans
    
            

def seq_search(x, y):
    minMAD = 1e9
    for i in range(x-15, x+16):
        if i < 0 or i >= img.shape[0]:
            continue
        for j in range(y-15, y+16):
            if j < 0 or j >= img.shape[1]:
                continue
            curMAD = MAD(x, y, i, j)
            if curMAD < minMAD:
                minMAD = curMAD
                u = i
                v = j
    return (u,v)

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        print ( seq_search(x, y) )
                
        

#img2 = cv2.imread("../Assignment3/images/i1.pgm")


#print(img.shape)
#print(img2.shape)
#print(img3.shape)


#cv2.imshow('image',img-img2)
#cv2.imshow('image1',img)
#cv2.imshow('image2',img2)
#cv2.imshow('image3',img3)
#cv2.imshow('image3',cv2.absdiff(img, img2))
cv2.waitKey(0)
cv2.destroyAllWindows()
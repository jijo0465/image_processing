import numpy as np
import cv2
from pip._vendor.distlib.compat import raw_input


def readAndDisplayColorImage(src):
    img = cv2.imread(src, cv2.IMREAD_COLOR)
    cv2.imshow('Color Image', img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()


def readAndDisplayGreyscaleImage(src):
    img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Greyscale Image', img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()


def addColorImages(src1, src2):
    img1 = cv2.imread(src1, cv2.IMREAD_COLOR)
    img2 = cv2.imread(src2, cv2.IMREAD_COLOR)
    addedImg = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)
    cv2.imshow('Added Color Image', addedImg)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()

def addGreyScaleImages(src1, src2):
    img1 = cv2.imread(src1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(src2, cv2.IMREAD_GRAYSCALE)
    addedImg = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)
    cv2.imshow('Added Greyscale Image', addedImg)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()

def subtractImages(src1, src2):
    image1 = cv2.imread(src1)
    image2 = cv2.imread(src2)
    sub = cv2.subtract(image1, image2)
    cv2.imshow('Subtracted Image', sub)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


print()
print('------------------------')
print('Digital Image Processing')
print('------------------------')
print()
print('1. Read and display Color Image')
print('2. Read and display Greyscale Image')
print('3. Add two color images')
print('4. Add two greyscale images')
print('5. Subtract two images')

k = cv2.waitKey(0) & 0xFF
n = int(raw_input())
if n == 1:
    readAndDisplayColorImage('bird.jpg')
if n == 2:
    readAndDisplayGreyscaleImage('bird.jpg')
if n == 3:
    addColorImages('add1.jpg', 'add2.jpg')
if n == 4:
    addGreyScaleImages('add1.jpg', 'add2.jpg')
if n == 5:
    subtractImages('sub1.jpg', 'sub2.jpg')

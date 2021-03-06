#!python
# -*- coding: utf-8 -*-

print("content-type: text/html; charset-utf-8\n")

import cgi
import cgitb    #스크립트 오류 등의 에러발생시 브라우저에 에러 내용을 보여준다.
cgitb.enable()
import matplotlib.pyplot as plt
import numpy as np

import cv2
import os
import requests
from bs4 import BeautifulSoup
import json
import sys

name = ["input/ret0.jpg",
        "input/ret1.jpg",
        "input/ret2.jpg",
        "input/ret3.jpg",
        "input/ret4.jpg",
        "input/ret5.jpg",
        "input/ret6.jpg",
        "input/ret7.jpg",
        "input/ret8.jpg",
        "input/ret9.jpg",
        "input/ret10.jpg",
        "input/ret11.jpg",
        "input/ret12.jpg",
        "input/ret13.jpg"]

form = cgi.FieldStorage()
number_img = int(form["input_num"].value)
store_name = "input/middle.jpg"

input_im = "input/opencv_ori.jpg"

OUTPUT_DIR = 'input/output11/'
MEAN_VALUES = np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3))

get_object = "input/get_object.jpg"
mix_img = "input/opencv.jpg"
water = "input/water.jpg"
total_ret = 0

def combine_two(input1, input2):
    # combine_two( wartershed(img),original)
    # original이 원본 , img = 변한 화면
    # img1 = cv2.imread(input1, -1)#검은배경화면
    # img2 = cv2.imread(input2, -1)#원본사진

    img1 = cv2.imread(input1)
    img2 = cv2.imread(input2)

    # 사진 크기 조절
    img1 = cv2.resize(img1, dsize=(300, 400))
    img2 = cv2.resize(img2, dsize=(300, 400))

    rows, cols, channels = (img1.shape)

    roi = img2[0:rows, 0:cols]

    img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

    mask_inv = cv2.bitwise_not(mask)

    img1_fg = cv2.bitwise_and(img1, img1, mask=mask)
    img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # 2개의 이미지를 합치면 바탕은 제거되고 logo부분만 합쳐짐.
    dst = cv2.add(img1_fg, img2_bg)

    # 합쳐진 이미지를 원본 이미지에 추가.
    img2[0:rows, 0:cols] = dst

    plt.imshow(img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    # 중간 파일 제거
    #os.remove('middle.jpg')

    # 마지막 파일 저장
    cv2.imwrite('input/Final.jpg', img2)
def wartershed(input_im):
    img = cv2.imread(input_im)
    img = cv2.resize(img, dsize=(300, 400))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)
    #print("the ret is ",ret)
    total_ret = ret
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [0, 0, 0]

    #want = input("원하는 번호를 입력하세요: ")
    want = 2
    ret = int(ret)
    for i in range(ret + 1):
        if i != int(want):
            img[markers == i] = [0, 0, 0]

    cv2.imwrite(name[want], img)
    return img

    """
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(ret)
    # markers==1 이면 배경
    ret = int(ret)
    for i in range(ret + 1):
        if i != 3:
            img[markers == i] = [0, 0, 0]
    """
    cv2.imwrite('input/water.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #return "get_object.jpg"
def obj_wartershed(input_im,want):
    img = cv2.imread(input_im)
    img = cv2.resize(img, dsize=(300, 400))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)
    #print("the ret is ", ret)
    total_ret = ret
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [0, 0, 0]

    ret = int(ret)
    for i in range(ret + 1):
        if i != int(want):
            img[markers == i] = [0, 0, 0]

    cv2.imwrite(name[want], img)
    return img

    """
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(ret)
    # markers==1 이면 배경
    ret = int(ret)
    for i in range(ret + 1):
        if i != 3:
            img[markers == i] = [0, 0, 0]
    """
    cv2.imwrite('input/water.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # return "get_object.jpg"
def make_obj_img(input, ret) :
    for i in range(ret):
        obj_wartershed(input,i+1)
def get_total_ret(input_im):
    img = cv2.imread(input_im)
    img = cv2.resize(img, dsize=(300, 400))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)
    return ret


#img = load_image(input_im)
#original = load_image(input_im)
#img = cv2.imread(input_im)
#original = cv2.imread(input_im)
#wartershed(input_im)
#make_obj_img(input_im,4)
#combine_two(get_object,mix_img)
total_ret = get_total_ret(input_im)
img = cv2.imread(name[number_img])
cv2.imwrite(store_name, img)

for i in  range(total_ret):
    os.remove(name[i+1])

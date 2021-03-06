#!python
print("content-type: text/html; charset-utf-8\n")
# -*- coding: utf-8 -*-

print("hello world")
"""
import cgi
import os
import json
import sys
"""
import cv2

input_im = "input/opencv_ori.jpg"
img2 = cv2.imread(input_im)
cv2.imwrite('input/Final.jpg', img2)
import numpy as np
import scipy.io
import scipy.misc
import tensorflow as tf  # Import TensorFlow after Scipy or Scipy will break
import matplotlib.pyplot as plt


"""
var_php = -1

if __name__ == '__main__':
    try:
        data = json.loads(sys.argv[1])
        print("hello")
        var_php = data


    except:
        print("ERROR")
        sys.exit(1)


print (data)
"""
OUTPUT_DIR = 'input/output11/'
MEAN_VALUES = np.array([123.68, 116.779, 103.939]).reshape((1,1,1,3))


get_object = "input/get_object.jpg"
mix_img = "input/opencv.jpg"
water = "input/water.jpg"
total_ret = 0
"""
name = ["C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret0.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret1.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret2.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret3.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret4.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret5.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret6.jpg",
        "C:\Bitnami\wampstack-7.1.29-0\apache2\htdocs\input\ret7.jpg"]

"""
name = ["input/ret0.jpg","input/ret1.jpg","input/ret2.jpg","input/ret3.jpg","input/ret4.jpg","input/ret5.jpg","input/ret6.jpg","input/ret7.jpg"]



def load_image(path):
    #image = scipy.misc.imread(path)
    image = cv2.imread(path)
    # Resize the image for convnet input, there is no change but just
    # add an extra dimension.
    image = np.reshape(image, ((1,) + image.shape))
    # Input to the VGG model expects the mean to be subtracted.
    image = image - MEAN_VALUES
    return image
def save_image(path, image):
    # Output should add back the mean.
    image = image + MEAN_VALUES
    # Get rid of the first useless dimension, what remains is the image.
    image = image[0]
    image = np.clip(image, 0, 255).astype('uint8')
    #scipy.misc.imsave(path, image)
    cv2.imwrite(path,image)
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
    print("the ret is ",ret)
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
    print("the ret is ", ret)
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

#img = load_image(input_im)
#original = load_image(input_im)
#img = cv2.imread(input_im)
#original = cv2.imread(input_im)

#wartershed(input_im)
make_obj_img(input_im,4)
#combine_two(get_object,mix_img)

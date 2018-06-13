# -*- coding: UTF-8 -*_
# 第二步
# 一次二值化两次中值滤波 图像处理 

import cv2
import numpy as np
from matplotlib import pyplot as plt  
import glob
import os
import os.path

# 中值滤波 
def I_threshold(GrayImage):
    GrayImage= cv2.medianBlur(GrayImage,5)  
    ret,th1 = cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY) 
    return th1
    pass


CAPTCHA_IMAGE_FOLDER = "src_img"
OUTPUT_FOLDER = "out_img"

captcha_image_files = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
counts = {}

for (i, captcha_image_file) in enumerate(captcha_image_files):
    print("[INFO] processing image {}/{}".format(i + 1, len(captcha_image_files)))

    filename = os.path.basename(captcha_image_file)
    captcha_correct_text = os.path.splitext(filename)[0]

    img = cv2.imread(captcha_image_file) 

    # 灰度化
    GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    
    #中值滤波两次
    th1 = I_threshold(GrayImage)

    # th2 = I_threshold(th1) 

    th3= cv2.medianBlur(th1,5)  

    th4= cv2.medianBlur(th3,5)  

    savefile = os.path.join(OUTPUT_FOLDER,filename)

    cv2.imwrite(savefile, th4)

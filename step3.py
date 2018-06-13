# -*- coding: UTF-8 -*_

# 图片找轮廓分割单个字符

import cv2
import numpy as np
from matplotlib import pyplot as plt  
import glob
import os
import os.path
import imutils


CAPTCHA_IMAGE_FOLDER = "out_img"
OUTPUT_FOLDER = "easy_img"

captcha_image_files = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
counts = {}

captcha_image_files=captcha_image_files

for (i, captcha_image_file) in enumerate(captcha_image_files):
   
    print("[INFO] processing image {}/{}".format(i + 1, len(captcha_image_files)))

    filename = os.path.basename(captcha_image_file)

    captcha_correct_text = os.path.splitext(filename)[0]

    image = cv2.imread(captcha_image_file) 

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Add some extra padding around the image
    gray = cv2.copyMakeBorder(gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)

    # threshold the image (convert it to pure black and white)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # find the contours (continuous blobs of pixels) the image
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Hack for compatibility with different OpenCV versions
    contours = contours[0] if imutils.is_cv2() else contours[1]

    # print(len(contours))
    letter_image_regions = []
    # 画出轮廓
    # cv2.drawContours(image,contours,-1,(0,0,255),3)  

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        # 大于长*宽大于100像素认为是字符
        if w * h >100:
            letter_image_regions.append((x,y,w,h))
            # print("x:{} y:{} w:{} h:{}".format(x, y, w, h))
            # 画出方框
            # cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 1)

    if len(letter_image_regions) != 4:
        continue
    # 数组拼接成元组 
    # print(list(zip(letter_image_regions, captcha_correct_text)))
    # 数组排序根据X
    letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])

    for letter_bounding_box, letter_text in zip(letter_image_regions, captcha_correct_text):
        # Grab the coordinates of the letter in the image
        x, y, w, h = letter_bounding_box
       
        # Extract the letter from the original image with a 2-pixel margin around the edge
        letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]

        # Get the folder to save the image in
        save_path = os.path.join(OUTPUT_FOLDER, letter_text)

        # if the output directory does not exist, create it
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # write the letter image to a file
        count = counts.get(letter_text, 1)
        p = os.path.join(save_path, "{}.png".format(str(count).zfill(6)))
        cv2.imwrite(p, letter_image)

        # increment the count for the current key
        counts[letter_text] = count + 1







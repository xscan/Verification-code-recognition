# 分割4字符验证码为单个小图片 -- 多线程

# 单个字符统一长度宽度为40px
# 数据归一
import cv2
import pickle
import os.path
import numpy as np
from imutils import paths
from helpers import resize_to_fit

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import freeze_support

from matplotlib import pyplot as plt 

import time

LETTER_IMAGES_FOLDER = "easy_img"
LETTER_IMAGES_FOLDER_YZH = 'normalizing_img'


# initialize the data and labels
data = []
labels = []
# print(list(paths.list_images(LETTER_IMAGES_FOLDER)))
pathlist=list(paths.list_images(LETTER_IMAGES_FOLDER))

row = len(pathlist)
col = len(pathlist)


global current
current = 0

def w1(func):
    def inner(*args,**kwargs):
        past = time.time()
        func(*args,**kwargs)
        now = time.time()
        cost_time = now - past
        print("The function <%s> cost time: <%s>"%(func.func_name,cost_time))
    return inner


def resizeImage(image_file):
    global current
    current=current+1
    print("[INFO] processing image {}/{}".format(current,row))

    image = cv2.imread(image_file)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = resize_to_fit(image, 20, 20)

    label = image_file.split(os.path.sep)[-2]

    save_path=os.path.join(LETTER_IMAGES_FOLDER_YZH,label)

    filename=image_file.split(os.path.sep)[-1]

    full_save_path = os.path.join(save_path,filename)
    # print(save_path)
    if not os.path.exists(save_path):
            os.makedirs(save_path)

    cv2.imwrite(full_save_path,image)


    


tpool = ThreadPool(8)
tpool4 = ThreadPool(4)

# 多线程
# @w1
def MulThread():
    for i in pathlist:
        tpool.apply(func=resizeImage,args=(i,))

    tpool.close()
    tpool.join()
    # print('20000 end')
    # 可能出现无法读取文件情况，是因为生成了错误图片文件产生
    # 25438
    # 25438+11655
    # for i in pathlist:
    #     tpool4.apply(func=resizeImage,args=(i,))

    # tpool4.close()
    # tpool4.join()
    pass

MulThread()

# print(pathlist[25436])
# print(pathlist[25437])
# print(pathlist[25438])

# print(pathlist[37092])
# print(pathlist[37093])
# print(pathlist[37094])
# print(pathlist[25438])
# 多进程
ppool = Pool(4)
# @w1
def MulProcess():
    for i in pathlist:
        ppool.apply(func=resizeImage,args=(i,))

    ppool.close()
    ppool.join()

# MulProcess()


# 分割4字符验证码为单个小图片
# 单个字符统一长度宽度为20px
# 数据归一
import cv2
import pickle
import os.path
import numpy as np
from imutils import paths
from helpers import resize_to_fit

from matplotlib import pyplot as plt 

LETTER_IMAGES_FOLDER = "easy_img"
LETTER_IMAGES_FOLDER_YZH = 'normalizing_img'


# initialize the data and labels
data = []
labels = []
# print(list(paths.list_images(LETTER_IMAGES_FOLDER)))
pathlist=list(paths.list_images(LETTER_IMAGES_FOLDER))[:4]
row = len(pathlist)
col = len(pathlist)
current = 1

# exit
# loop over the input images
for image_file in pathlist:
    # Load the image and convert it to grayscale
    print("[INFO] processing image {}/{}".format(current, len(pathlist)))
    image = cv2.imread(image_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plt.subplot(row,col,current)
    plt.imshow(image,'gray')  

    # Resize the letter so it fits in a 20x20 pixel box
    image = resize_to_fit(image, 20, 20)

    plt.subplot(row,col,current+col)
    plt.imshow(image,'gray') 
   
    current=current+1
    # Add a third channel dimension to the image to make Keras happy
    # image = np.expand_dims(image, axis=2)


    # Grab the name of the letter based on the folder it was in
    label = image_file.split(os.path.sep)[-2]
    
    save_path=os.path.join(LETTER_IMAGES_FOLDER_YZH,label)
    filename=image_file.split(os.path.sep)[-1]
    full_save_path = os.path.join(save_path,filename)
    # print(save_path)
    if not os.path.exists(save_path):
            os.makedirs(save_path)

    cv2.imwrite(full_save_path,image)
    # Add the letter image and it's label to our training data
    data.append(image)
    labels.append(label)


# plt.show()


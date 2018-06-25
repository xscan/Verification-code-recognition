# 使用模型
from keras.models import load_model
from helpers import resize_to_fit
from imutils import paths
import numpy as np
import imutils
import cv2
import pickle
import os

import os.path

# import numpy as np
from matplotlib import pyplot as plt  
# 中值滤波 
def I_threshold(GrayImage):
    GrayImage= cv2.medianBlur(GrayImage,5)  
    ret,th1 = cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY) 
    return th1
    pass

MODEL_FILENAME = "captcha_model.hdf5"
MODEL_LABELS_FILENAME = "model_labels.dat"
CAPTCHA_IMAGE_FOLDER = "test_img"


# Load up the model labels (so we can translate model predictions to actual letters)
with open(MODEL_LABELS_FILENAME, "rb") as f:
    lb = pickle.load(f)

# Load the trained neural network
model = load_model(MODEL_FILENAME)

success = 0
error = 0
captcha_image_files = list(paths.list_images(CAPTCHA_IMAGE_FOLDER))[1:1000]
# captcha_image_files = np.random.choice(captcha_image_files, size=(10,), replace=False)

print(captcha_image_files)


for image_file in captcha_image_files:
    # 
    predictions = []
    counts = {}
    # Load the image and convert it to grayscale
    image = cv2.imread(image_file)
    # print(image)
    if image is None:
        continue
        pass
    
    # 灰度化
    GrayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    
    #中值滤波两次
    th1 = I_threshold(GrayImage)

    th2= cv2.medianBlur(th1,5)  

    th3= cv2.medianBlur(th2,5)  

    gray = th3

    filename = os.path.basename(image_file)

    captcha_correct_text = os.path.splitext(filename)[0]
    print(captcha_correct_text)
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


         # Re-size the letter image to 20x20 pixels to match training data
        letter_image = resize_to_fit(letter_image, 20, 20)

        # Turn the single image into a 4d list of images to make Keras happy
        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)

        # Ask the neural network to make a prediction
        prediction = model.predict(letter_image)

        # Convert the one-hot-encoded prediction back to a normal letter
        letter = lb.inverse_transform(prediction)[0]
        predictions.append(letter)
        # write the letter image to a file
        count = counts.get(letter_text, 1)
        counts[letter_text] = count + 1


    captcha_text = "".join(predictions)
    print("CAPTCHA text is: {}".format(captcha_text))
    # print(type(captcha_correct_text))
    # print(type(captcha_text))
    if captcha_text == captcha_correct_text:
        success = success +1
    else:
        error =error +1
        pass
    cv2.waitKey()
    # plt.imshow(th3,'gray')
    # plt.show()
print("sum:{} \n success:{} \n error:{} \n success/sum:{}".format(success+error,success,error,success/(success+error)*100))
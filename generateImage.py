# -*- coding: UTF-8 -*_
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

import time

import os

import os.path

save_path='test_img'
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60

generateNum=5000
for i in range(generateNum):
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('msyh.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    strtmp=''
    for t in range(4):
        tmprndChar=rndChar()
        strtmp=strtmp+tmprndChar
        draw.text((60 * t + 10, 10), tmprndChar, font=font, fill=rndColor2())
    # 模糊:
    #image = image.filter(ImageFilter.BLUR)
    savefile=os.path.join(save_path,strtmp+'.jpg')
    # print(savefile)
    image.save(savefile, 'jpeg')
    print("vcode:{}  {}/{}".format(strtmp,i,generateNum))
  

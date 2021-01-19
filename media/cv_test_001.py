# -*- coding: UTF-8 -*-
import cv2
from PIL import Image, ImageDraw, ImageFont

img = cv2.imread("0.bmp")
#原图灰度转换
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

for i in range(1, 6):
    t1=cv2.cvtColor(cv2.imread(str(i)+".bmp"),cv2.COLOR_RGB2GRAY)

    #直方图计算的函数，反应灰度值的分布情况
    hist = cv2.calcHist([gray], [0], None, [256], [0.0,255.0])

    h1 = cv2.calcHist([t1], [0], None, [256], [0.0,255.0])
    #相关性计算，采用相关系数的方式
    result = cv2.compareHist(hist,h1,method=cv2.HISTCMP_CORREL)
    im = Image.open(str(i) + ".bmp")

    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype(r'C:\Windows\Fonts\simsun.ttc', 30)
    #这里视作》=0.9认为相似，即合格
    if result >=0.9:
        draw.text((5, 10), u'合格', fill='red', font=fnt)
    else:
        draw.text((5, 10), u'不合格', fill='red', font=fnt)
    im.show("result" +str(i) + ".png")
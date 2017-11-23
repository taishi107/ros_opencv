#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys,rospy
import pytesseract
from PIL import Image

mirror = True
size = None

#カメラをキャプチャする
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    #フレームをリサイズ
    if size is not None and len(size) == 2:
        frame = cv2.resize(frame, size)

    #フレームを表示
    cv2.imshow('camera capture', frame)
    k = cv2.waitKey(1)
    
    #カメラから画像を取得(q)
    if k==113:
        path = "data.jpg"
        cv2.imwrite(path,frame)
        photo = path
        img_src = cv2.imread(photo)
        img = cv2.cvtColor(img_src, cv2.COLOR_RGB2GRAY)
        url_img = photo
        img = Image.open(url_img)
        number = pytesseract.image_to_string(img)
    if k==27:
	break
cap.release()
cv2.destroyAllWindows()

#自動撮影
import cv2
import datetime
from time import time
import os


# 使用カメラ指定(カメラ番号注意)
deviceid=0
capture = cv2.VideoCapture(deviceid)


ret, frame = capture.read()
strdate=datetime.datetime.now().strftime('%Y%m%d_%H%M')
path='./media/'+strdate+'.jpg'
path2='./Movies_Ph/'+strdate+'.jpg'
cv2.imwrite(path,frame)
cv2.imwrite(path2,frame)
print("正常に撮影できました。")


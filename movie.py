#動画作成
import glob
import datetime
import cv2
import os
import shutil

img_array = []
for filename in sorted(glob.glob('Movies_Ph/*.jpg')):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

strdate=datetime.datetime.now().strftime('%Y_%m%d')
name = "./Movies/Movie"+strdate+".mp4"
out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'H264'), 3.0, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

#動画作成ファイルクリア
shutil.rmtree('Movies_ph')
os.mkdir('Movies_ph')
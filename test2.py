# jhgjhgjhgjh
import cv2 as cv
import numpy as np
import os

fp = open("20180719_IMG_1229.JPG", "r")  # 打开文件读取所有内容
while 1:
    line = fp.readline()  # 一行一行的存储读取的文件
    if not line:
        break  # line为空结束循环
    str1 = line.split()  # 将line中的数据切分存储在数组str1中
path = cv.imread(str1[0])  # 待处理的图像名
facenumber = int((len(str1) - 1) / 16)  # 人脸的个数
count = 1  # 以此为读取矩形框数据的循环的起点
for i in range(facenumber):  # 依次对每张人脸画矩形框
    x = int(str1[count + 1])
    y = int(str1[count + 2])
    wideth = int(str1[count + 3])
    higeth = int(str1[count + 4])
    cv.rectangle(path, (x, y), (x + wideth, y + higeth), (255, 255, 255), 10, 8, 0)  # 画矩形框
    count += 16  # str1的下一个矩形数据组
cv.namedWindow("resultpicture")  # 打开显示图形界面
cv.imshow("resultpicture", path)  # 显示结果图像
cv.waitKey(0)
cv.imwrite("./result_labelFace.jpg", path)  # 存储结果图像

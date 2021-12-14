import os
import time
import cv2
import numpy as np
# import face_recognition

path = os.getcwd().replace('\\', '/') + '/ImagesStudent'
images = []
class_names = []

file_list = os.listdir(path)
for file in file_list:
    img = cv2.imread(f'{path}/{file}')
    images.append(img)
    class_names.append(file.split('.')[0])









# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList
# print(path)
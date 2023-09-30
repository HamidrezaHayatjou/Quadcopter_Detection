import cv2
from matplotlib import pyplot as plt
import numpy as np
import glob
import os



def summarisevideo(videofile,PATH):
    path = PATH + "/%d.jpg"
    video_v = cv2.VideoCapture(videofile)
    video_w = int(video_v.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_h = int(video_v.get(cv2.CAP_PROP_FRAME_HEIGHT))
    u = 0 #unique frame counter
    thres = 105
    status_v, frame1_v = video_v.read()
    previous_f = frame1_v
    cv2.imwrite(path %u, frame1_v)
    while True:
        status_v, current_f = video_v.read()
        if status_v is True:
            frame_diff = np.sum(np.absolute(current_f - previous_f)) / np.size(current_f)
            if(frame_diff > thres):
                cv2.imwrite(path %u, current_f)
                previous_f = current_f
                u = u + 1 
            else:
                pass
        else: 
            break
#     print("total no. of unique frames: ", u)
    video_v.release()
    
    

def createvideo(PATH):
    path = PATH + "/*.jpg"
    img_array = []
    x=glob.glob(path)
    x.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    for filename in x:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    out = cv2.VideoWriter('summvid.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v') , 25, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    
    

# Motion Detection
# https://software.intel.com/en-us/node/754940

import numpy as np
import cv2
from datetime import datetime

def distMap(frame1, frame2):
    """outputs pythagorean distance between two frames"""
    frame1_32 = np.float32(frame1)
    frame2_32 = np.float32(frame2)    
    diff32 = frame1_32 - frame2_32
    num = np.sqrt(diff32[:, :, 0]**2 + diff32[:, :, 1]**2 + diff32[:, :, 2]**2)
    den = np.sqrt(255**2 + 255**2 + 255**2)
    norm32 = num / den
    dist = np.uint8(norm32 * 255)
    return dist

sdThresh = 5
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.namedWindow('frame')
cv2.namedWindow('dist')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (500,450))

_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    ret, frame3 = cap.read()
    if ret:
        rows, cols, _ = np.shape(frame3)
        dist = distMap(frame1, frame3)

        frame1 = frame2
        frame2 = frame3

        # apply Gaussian smoothing
        mod = cv2.GaussianBlur(dist, (7, 7), 0)

        _, thresh = cv2.threshold(mod, 100, 255, 0)

        _, stDev = cv2.meanStdDev(thresh)
#         print(stDev)

        cv2.imshow('dist', mod)
        cv2.putText(frame1, "Standard Deviation - {}".format(round(stDev[0][0],0)), (70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA)
        if stDev > sdThresh:
            print('Motion Detected : ', datetime.now().strftime("%B %d %Y %H:%M:%S"))
#             out.write(frame2)                
        cv2.imshow('frame', frame2)
        
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()

                     
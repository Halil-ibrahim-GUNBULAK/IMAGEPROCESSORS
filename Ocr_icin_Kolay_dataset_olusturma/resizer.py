## Bulk image resizer

# This script simply resizes all the images in a folder to one-eigth their
# original size. It's useful for shrinking large cell phone pictures down
# to a size that's more manageable for model training.

# Usage: place this script in a folder of images you want to shrink,
# and then run it.

import numpy as np
import cv2
import os

dir_path = os.getcwd()
i=76
for filename in os.listdir(dir_path):
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith(".png"):
        image = cv2.imread(filename)
        resized110 = cv2.resize(image, None, fx=1.10, fy=1.10, interpolation=cv2.INTER_AREA)
        resized120 = cv2.resize(image, None, fx=1.20, fy=1.20, interpolation=cv2.INTER_AREA)
        resized130 = cv2.resize(image, None, fx=1.30, fy=1.30, interpolation=cv2.INTER_AREA)
        resized140 = cv2.resize(image, None, fx=1.40, fy=1.40, interpolation=cv2.INTER_AREA)
        resized150= cv2.resize(image, None, fx=1.50, fy=1.50, interpolation=cv2.INTER_AREA)


        img1 = resized110[1:29, 1:29]
        img2 = resized120[3:31,3:31]
        img3 = resized130[4:32, 4:32]
        img4 = resized140[6:34, 6:34]
        img5 = resized150[7:35, 7:35]

        ss = 'a ({}).png '.format(i)
        cv2.imwrite(ss, img1)
        i=i+1
        ss = 'a ({}).png '.format(i)
        cv2.imwrite(ss, img2)
        i = i + 1
        ss = 'a ({}).png '.format(i)
        cv2.imwrite(ss, img3)
        i = i + 1
        ss = 'a ({}).png '.format(i)
        cv2.imwrite(ss, img4)
        i = i + 1
        ss = 'a ({}).png '.format(i)









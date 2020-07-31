import pandas as pd
import glob
import cv2
import pandas as pd
import requests
i=0

array=['ab','bb','db','eb','fb''gb','hb','ib']
dosya1=cv2.imread("dene.png")
dosya2=cv2.imread("ikinci.png")
dosya3=cv2.imread("ucuncu.png")
yuk,gen=dosya1.shape[0:2]

print(dosya1.shape[0:2])
for sutun in range(0,int(gen/28)):
 for satır in range(0,int(yuk/28)):

    try:

        img1 = dosya1[satır*28:(satır+1)*28, sutun*28:(sutun+1)*28]
        #img2= dosya2[satır*28:(satır+1)*28, sutun*28:(sutun+1)*28]
        #img3 = dosya3[satır * 28:(satır + 1) * 28, sutun * 28:(sutun + 1) * 28]
        cv2.imwrite('C:/tensorflow1/models/research/object_detection/resim_kirpma/train/ t'+str(i)+'.png', img1)
        i = i + 1
       # cv2.imwrite('t' + str(i) + '.png', img2)
        #i=i+1
        #cv2.imwrite('t' + str(i) + '.png', img3)
        #i = i + 1
    except:
        print('Image {0} not downloaded'.format(sutun))
        continue

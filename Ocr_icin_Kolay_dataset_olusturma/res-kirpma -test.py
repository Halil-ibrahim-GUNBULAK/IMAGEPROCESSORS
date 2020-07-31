import pandas as pd
import glob
import cv2
import pandas as pd
import requests
i=0

c=-1
array=['ab','bb','db','eb','fb','gb','hb','ib','kb','lb','mb','nb','pb','qb','rb','tb',
       'yb','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w'
       ,'x','y','z','1','2','3','4','5','6','7','8','9','0','oo','uu','ss','cc']

arrayres=['test1','test2','test3','test4','test5','test6','test7','test8','test9','test10','test11','test12',
          'test13','test14','test15','test16']
arrayden=['test2','test3','test5','test7']

arrayi=[0,125,250,375,500,625,750,875,1000,1125,1250,1375,1500,1625,1750,1875]

arraya=[0,25,50,75,100,125,150,175,200,225,250,275,300,375,400,425,450,475]
for k in arrayres:
 c=c+1
 dosya1=cv2.imread("{}.png".format(k))

 yuk,gen=dosya1.shape[0:2]
 print(dosya1.shape[0:2])
 for sutun in range(0,int(gen/28)):
  i=arrayi[c]
  print(arrayi[c])
  a=arraya[c]
  for satır in range(0,int(yuk/28)):

     try:
        # resi i burda yap daha mantıklı
        img1 = dosya1[satır*28:(satır+1)*28, sutun*28:(sutun+1)*28]

        cv2.imwrite('C:/tensorflow1/models/research/object_detection/kerasimage/train/'+array[sutun]+'/'+ array[sutun]+' ('+str(i)+').png', img1)

        cv2.imwrite('C:/tensorflow1/models/research/object_detection/kerasimage/train/{}' + array[sutun] + ' (' + str(
            a) + ').png', img1)
        a = a + 1

        i = i + 1


        resized110 = cv2.resize(img1, None, fx=1.10, fy=1.10, interpolation=cv2.INTER_AREA)
        resized120 = cv2.resize(img1, None, fx=1.20, fy=1.20, interpolation=cv2.INTER_AREA)
        resized130 = cv2.resize(img1, None, fx=1.30, fy=1.30, interpolation=cv2.INTER_AREA)
        resized140 = cv2.resize(img1, None, fx=1.40, fy=1.40, interpolation=cv2.INTER_AREA)

        img = resized110[1:29, 1:29]
        img2 = resized120[3:31, 3:31]
        img3 = resized130[4:32, 4:32]
        img4 = resized140[6:34, 6:34]


        ss = 'C:/tensorflow1/models/research/object_detection/kerasimage/train/'+array[sutun]+'/'+ array[sutun]+' ('+str(i)+').png'
        cv2.imwrite(ss, img)
        i = i + 1
        ss = 'C:/tensorflow1/models/research/object_detection/kerasimage/train/'+array[sutun]+'/'+ array[sutun]+' ('+str(i)+').png'
        cv2.imwrite(ss, img2)
        i = i + 1
        ss = 'C:/tensorflow1/models/research/object_detection/kerasimage/train/'+array[sutun]+'/'+ array[sutun]+' ('+str(i)+').png'
        cv2.imwrite(ss, img3)
        i = i + 1
        ss = 'C:/tensorflow1/models/research/object_detection/kerasimage/train/'+array[sutun]+'/'+ array[sutun]+' ('+str(i)+').png'
        cv2.imwrite(ss, img4)
        i = i + 1


     except:
         print('Image {0} not downloaded'.format(sutun))
         continue

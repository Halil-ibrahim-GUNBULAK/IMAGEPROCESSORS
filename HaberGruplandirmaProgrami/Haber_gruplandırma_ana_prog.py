import  numpy as np
import cv2
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from matplotlib import pyplot as plt
import numpy as np
from nltk.corpus import stopwords
import nltk
from kelimekokubulma import kokbulma



model = Word2Vec.load('30vec.model')
stopwords = stopwords.words('turkish')

Spor         =['12/spor', 'voleybol', 'boks', 'hakem', 'basketbol', 'maç', 'hentbol', 'futbol', 'takım', 'taraftar'                         ]
Cevre        =['13/cevre', 'deniz', 'rüzgâr', 'ekosistem', 'Enerjiyi', 'sahil', 'kirlilik', 'bitki', 'toprak', 'habitat'                    ]
Ekonomi      =['5/ekonomi', 'kur', 'makro', 'risk', 'kriz', 'durgunluk', 'çöküntü', 'ekonomik', 'buhran', 'Maliye'                          ]
Dunya        =['6/dunya','Brezilya', 'devletler',  'batı', 'Müslüman', 'Avrupa', 'dünya', 'Asya', 'Afrika', 'ABD'                           ]
Medya        =[ '8/medya','hesap', 'medya', 'kullanıcı', 'paylaşım', 'instagram', 'twitter', 'facebook', 'youtube', 'video'                 ]
İsciSendika  =['2/isci-sendika','işçi', 'patron',  'SF', 'Ücret', 'emekçi', 'işvereni', 'Grev', 'izin', 'Fabrika'                           ]
Bolge        =[ '4/bolge','Türkiye', 'ordu', 'üs', 'asker', 'Operasyon', 'güneybatı', 'bölge', 'kuzeybatısında', 'Güvenli'                  ]
Yasam        =[ '11/yasam','yaşam', 'yitirmişti', 'kaybet', 'hayat', 'öldüğü', 'yaralandığı', 'mülteci/göçmen', 'Ünlü', 'Çatışmada'         ]
Politika     =['3/politika','politika', 'İktidar', 'kapitalist', 'başkanlık', 'hükümet',  'ülkemiz', 'tutsaklık', 'konjonktürel', 'siyaset' ]


class habersiniflandirma():


  def metin(a):
    toplamDegerKumesi = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sonhali=[]
    counter=0
    çarpım=1.0

    for i in range(len(a)):
              if a[i] not in stopwords:
                 sonhali.append(a[i])

    for i in range(len(sonhali)):
        sonhal=kokbulma.kelime(sonhali[i])
        bolgeToplam=0
        sporToplam=0
        politikaToplam=0
        cevreToplam=0
        ekonomiToplam=0
        dunyaToplam=0
        medyaToplam=0
        isciToplam=0
        yasamToplam=0
        
        try:
         model.wv.distance(sonhal,'spor')
         for k in range(10):

            yakinkelime =(model.wv.similarity(sonhal,Spor[k]))
            sporToplam=sporToplam+yakinkelime
            yakinkelime =(model.wv.similarity(sonhal,Politika[k]))
            politikaToplam =politikaToplam + yakinkelime
            yakinkelime =(model.wv.similarity(sonhal,Cevre[k]))
            cevreToplam=cevreToplam + yakinkelime
            yakinkelime = (model.wv.similarity(sonhal,Ekonomi[k]))
            ekonomiToplam = ekonomiToplam + yakinkelime
            yakinkelime = (model.wv.similarity(sonhal,Dunya[k]))
            dunyaToplam = dunyaToplam + yakinkelime
            yakinkelime =  (model.wv.similarity(sonhal,Medya[k]))
            medyaToplam = medyaToplam + yakinkelime
            yakinkelime =(model.wv.similarity(sonhal, İsciSendika[k]))
            isciToplam =  isciToplam+ yakinkelime
            yakinkelime =  (model.wv.similarity(sonhal, Bolge[k]))
            bolgeToplam = bolgeToplam + yakinkelime
            yakinkelime = (model.wv.similarity(sonhal, Yasam[k]))
            yasamToplam = yasamToplam + yakinkelime

        except KeyError:
            counter=counter+1
            print(sonhal+" kelimesi uygun olmadığı için atlandı")
        print('İşlem Başarıyla Devam Ediyor Lütfen Bekleyiniz...')
        toplamDegerKumesi[0]= toplamDegerKumesi[0] + sporToplam
        toplamDegerKumesi[1]= toplamDegerKumesi[1] + politikaToplam
        toplamDegerKumesi[2]= toplamDegerKumesi[2] + cevreToplam
        toplamDegerKumesi[3]= toplamDegerKumesi[3] + ekonomiToplam
        toplamDegerKumesi[4]= toplamDegerKumesi[4] + dunyaToplam
        toplamDegerKumesi[5]= toplamDegerKumesi[5] + medyaToplam
        toplamDegerKumesi[6]= toplamDegerKumesi[6] + isciToplam
        toplamDegerKumesi[7]= toplamDegerKumesi[7] + yasamToplam
        toplamDegerKumesi[8]= toplamDegerKumesi[8] + bolgeToplam
    toplam=0
    for g in range(len(toplamDegerKumesi)):
        toplam=toplam+toplamDegerKumesi[g]
    for g in range(len(toplamDegerKumesi)):

      if toplamDegerKumesi[g]/toplam < 11.5/100:
          toplamDegerKumesi[g]=0

    return toplamDegerKumesi



  # most similar ile kelimenize yakın olan kelimeleri görüp listeye ekleyebilirsiniz
  def anahtarKelimeOlusturma(a,b):
      #a kelime b ise hangi listeye eklenmek istendiği
      kellis=[]
      close_words=model.wv.most_similar(a,topn=4)

      for i, _n in close_words:

              b.append(i)





  def sonucu_goster(list):
      listolusturma=('spor','politika','çevre','ekonomi','dünya','medya','işçi','yaşam','bölge')
      donenListe = []
      list_max = 0
      list_max_index = 0
      list_max2 = 0
      list_max2_index = 0



      for i in range(len(list)):
          if list[i] > list_max:
              list_max = list[i]
              list_max_index = i

      for i in range(len(list)):

          if list[i] > list_max2 and list[i] < list_max:
              list_max2 = list[i]
              list_max2_index = i

      fig = plt.figure()
      ax = fig.add_axes([0, 0, 1, 1])
      ax.axis('equal')
      deger = ['spor','politika','çevre','ekonomi','dünya','medya','işçi','yaşam','bölge']
      aldıgıpuan =[list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8]]
      ax.pie(aldıgıpuan, labels=deger, autopct='%1.2f%%')
      plt.savefig('hi.png')
      img=cv2.imread('hi.png')
      img=cv2.resize(img,None,fx=0.75,fy=0.75,interpolation=cv2.INTER_CUBIC)
      cv2.imwrite("hi.png",img)
      #plt.show()
      if list_max2!=0:
       print(str(listolusturma[list_max_index])+'='+str(list_max)+','+ str(listolusturma[list_max2_index])+'='+str(list_max2))
      if list_max2 == 0:
          print(str(listolusturma[list_max_index]) + '=' + str(list_max))
      return (listolusturma[list_max_index])





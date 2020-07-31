from kelimekokubulma import kokbulma
from nltk.corpus import stopwords
from kelimeturbulma import morfoloji
stopwords=stopwords.words('turkish')
import string
#şimdi özel isimleri bulan seti import edip özel isimleri çıkartıcaz
# çıkartmayada biliriz ama çıkartmazsak kelime atlamayı bulmamız lazım bulamazsak böyle bir yöntem uygulayabiliriz

class haber:
 #gelen text array olmalı
 def haberduzenleme(text):
    habertext=[]
    for i in range(len(text)):
     kelimemiz=kokbulma.kelime(text[i])
     if kelimemiz not in stopwords:
         habertext.append(kelimemiz)
     else: print("kelime stopwords")


    return habertext
 #istediğimiz tür kelimeleri haber text'inde aratmamızı sağlıyor
 def haberduzenlememorfolojik(text,tur):
    habertext=[]
    for i in range(len(text)):
     kelimemiz=kokbulma.kelime(text[i])
     if kelimemiz not in stopwords:
        if morfoloji.kelimeturu(kelimemiz)==morfoloji.kelimeturu(tur):
             habertext.append(kelimemiz)




    return habertext
#array olarak metini almaktadır
 #burda liste yapmamızın amacı içermeyen kelimeleride dönderebilirmek
 def metinDuzenleme(text):
     metinText=[]
     #metindeki kelimeleri aldık
     for i in range(len(text)):
         #kelimelerdeki harfleri aldık
         a=len(metinText)
         for k in range(len(text[i])):
             if text[i][k]=="'" or text[i][k]=='’' or text[i][k]=='!'or text[i][k]=="." or  text[i][k]=="," or text[i][k]==':' or text[i][k]==';':

               metinText.append(text[i][0:k])
                 # burdaki algoritma biz zaten gelen kelime uzunluğunu biliyoruz “ işarete raslayınca onu atlayıp geri kalan kelimeyi alıyoruz
             if text[i][k]=="“":
               metinText.append((text[i][1:len(text[i])]))
              #zor olan kısmı " için yapmak  cünkü kelimenin başındamı sonundamı karar vermesi gereken bilgisayar olucak
              # mesela "kelime......kelime" iki şekildede olabilir bu yüzden bir sonraki harf len(text[i]) içindeyse başta
              #dışındaysa sonda olduğunu anlayıp buna göre yazıcaz k+1 kullandık çünkü k range(0 dan 7 )ye diyelim k en fazla 6 oluyor
             if text[i][k]=='"' and k+1< len(text[i]):
               metinText.append((text[i][1:len(text[i])]))
             elif text[i][k]=='"' and k+1==len(text[i]):
               metinText.append((text[i][0:k]))
         if a==len(metinText):
             metinText.append(text[i])
     return  metinText


def corpusDeneme():
    def metinDuzenleme(text):
        metinText = []
        # metindeki kelimeleri aldık
        for i in range(len(text)):
            # kelimelerdeki harfleri aldık
            a = len(metinText)
            for k in range(len(text[i])):
                if text[i][k] == "'" or text[i][k] == '’'or text[i][k] == "." or text[i][k] == ","  or text[i][ k] == ':' \
                        or text[i][k] == ';':
                    metinText.append(text[i][0:k])
                    # burdaki algoritma biz zaten gelen kelime uzunluğunu biliyoruz “ işarete raslayınca onu atlayıp geri kalan kelimeyi alıyoruz
                if text[i][k] == "“":
                    metinText.append((text[i][1:len(text[i])]))
                # zor olan kısmı " için yapmak  cünkü kelimenin başındamı sonundamı karar vermesi gereken bilgisayar olucak
                # mesela "kelime......kelime" iki şekildede olabilir bu yüzden bir sonraki harf len(text[i]) içindeyse başta
                # dışındaysa sonda olduğunu anlayıp buna göre yazıcaz k+1 kullandık çünkü k range(0 dan 7 )ye diyelim k en fazla 6 oluyor
                if text[i][k] == '"' and k + 1 < len(text[i]):
                    metinText.append((text[i][1:len(text[i])]))
                elif text[i][k] == '"' and k + 1 == len(text[i]):
                    metinText.append((text[i][0:k]))
            if a == len(metinText):
                metinText.append(text[i])
        return metinText

#print(haber.metinDuzenleme(["'murat.","hasive,",'ceylan:',"metin;"]))
# Metin düzenleme Array geen bir dizi için kullanılıyor bu yüzden dolayı önce haber düzenleme daha sonra metin düzenleme şeklinde kullanılması
# yada text.split(' ') boşluklara göre texti ayırıp  sonra metin düzenlemesi yapılması önerilir herhangi bir array şeklinde metin göndersenizde tabiki kullanılır


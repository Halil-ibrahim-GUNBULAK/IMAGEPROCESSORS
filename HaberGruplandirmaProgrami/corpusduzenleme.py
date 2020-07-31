import string
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from kelimekokubulma import kokbulma
from kelimeturbulma import morfoloji
from haber_aktarma import haber

c=open('corpusdene.txt','r',encoding='utf8')
f=open('corpusduzenli.txt','a',encoding='utf8')
text=c.read()
text=text.split()
text=haber.haberduzenleme(text)

def corpusDuzenleme(text):
    metinText = []
    test = ''
    # metindeki kelimeleri aldık
    for i in range(len(text)):
        # kelimelerdeki harfleri aldık
        a = len(metinText)

        for k in range(len(text[i])):
            if text[i][k] == "'" or text[i][k] == "." or text[i][k] == "," or text[i][k] == '’' or text[i][k] == ':' or \
                    text[i][k] == ';' or text[i][k] == '”' or  text[i][k] == '>':
                metinText.append(text[i][0:k])
                test = test + str(text[i][0:k])+' '
                # burdaki algoritma biz zaten gelen kelime uzunluğunu biliyoruz “ işarete raslayınca onu atlayıp geri kalan kelimeyi alıyoruz
            if text[i][k] == "“" or  text[i][k] == '<':
                metinText.append((text[i][1:len(text[i])]))
                test=test+(str(text[i][1:len(text[i])]))+' '
            # zor olan kısmı " için yapmak  cünkü kelimenin başındamı sonundamı karar vermesi gereken bilgisayar olucak
            # mesela "kelime......kelime" iki şekildede olabilir bu yüzden bir sonraki harf len(text[i]) içindeyse başta
            # dışındaysa sonda olduğunu anlayıp buna göre yazıcaz k+1 kullandık çünkü k range(0 dan 7 )ye diyelim k en fazla 6 oluyor
            if text[i][k] == '"' and k + 1 < len(text[i]):
                metinText.append((text[i][1:len(text[i])]))
                test = test + str((text[i][1:len(text[i])]))+' '
            elif text[i][k] == '"' and k + 1 == len(text[i]):
                metinText.append((text[i][0:k]))
                test=test+str(text[i][0:k])+' '

        if a == len(metinText):
            metinText.append(text[i])
            test = test + str(text[i])+' '
    return test

f.write(corpusDuzenleme(text))






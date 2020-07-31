import  numpy as np
from nltk.corpus import stopwords

from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
model=Word2Vec.load('word2vec.model')
stopwords=stopwords.words('turkish')
a=model.wv.most_similar('çünkü')
# bu dosya stopwordsleri yani bağlaçları çünkü gibi edatları kaldırmak için yazılmıştır

benzerkelimeler=[]
atilankelime=[]
print(stopwords)
for i in range(len(a)):
 if i%2==0:
  for word in a[i]:

    if word not in stopwords:
        benzerkelimeler.append(word)
    else:
        atilankelime.append(word)
print(benzerkelimeler)
print(atilankelime)

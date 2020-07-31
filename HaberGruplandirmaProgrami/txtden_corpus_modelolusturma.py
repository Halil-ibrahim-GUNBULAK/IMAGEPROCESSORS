import  numpy as np
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt



f=open('corpusduzenli.txt','r',encoding='utf8')
text=f.read()
t_list=text.split('*')

corpus=[]

for cumle in t_list:
        corpus.append(cumle.split())
print(corpus[0:3])
model=Word2Vec(corpus,size=50,window=3,min_count=2,sg=1)
model.save('50vec.model')

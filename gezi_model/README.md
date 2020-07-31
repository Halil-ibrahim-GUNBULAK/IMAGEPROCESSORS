# Data Seti Hakkında
Data seti 13 bin turizim haberi 800 gezi makalesinden oluşan Türkiyenin şehirleri ile alakalı turizm ile alakalı oluşturulmuş bir modeldir 
Corpusunda 1.5 milyondan fazla kelime bulunmaktadır.Corpusundaki haberlerin haber sitesine ve makalelerin aldığımız siteye ait olmasından dolayı telif hakları bulunuyor bu yüzden corpusu paylaşmadık.
-30vec3window.model 30 vec 30 vectörlü olduğunu 3 windows ise skip gram algoritmasiyla 3 pencere sağdaki ve 3 pencere soldaki kelimeyi aldığını gösteriyor.
# Data Setini Nasıl Kullanabilirim
-model_deneme.py dosyasını açın 

```from gensim.models import Word2Vec
model = Word2Vec.load('TurkGezi75vec5window.model')
listisim=['Erzurum','Konya','Antalya','Bursa','İstanbul','Adana']
for i in listisim:
  model.wv.similarty(i,'kumsal')
  ```
 model başarısını ölçmek için yukarıdaki kodu girin kumsal bulunan şehirlerde değerin yüksek çıktığını bulunmayan şehirlerde ise daha düşük çıktığını gözlemleyebilirsiniz.

# Model ile geliştirilebilinecek projeler 
 -[Haber Gruplandırma](https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/tree/master/HaberGruplandirmaProgrami) projesinde olduğunu gibi doğal bir sinir ağı oluşturup modeli sınıflandırma için kullanabilirsiniz




<img src="https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/blob/master/HaberGruplandirmaProgrami/simge.png" width="400" height="200">

# Programın Amacı ve İşlevi

- Haber Gruplandırma programı ismindende anlaşılacağı üzere türkçe haberleri 9 gruba ayırmaya yarayan, insan hayatını kolaylaştıran bir programdır.<br/>
- Programın genel amacı insanların daha çabuk istediği türdeki haberlere ulaşması ve bazi haber sitelerinin daha fazla okunsun diye yanlış gruplandırılmış haberlerinin aslında hangi grupta olduğunu bulmak.<br/>
- Geçen yıl AçıkHack yarışmasında 1. olan Summarify program ile birleştirilip kişinin hangi haber türünü beğenip , beğenmediğini yüzde oranıyla değerlendirip daha sağlıklı  kişinin seveceği şekilde Summarify sana özel kısmı düzenlenebilir.
- HaberGruplandırma programı uzun metinlerde %98 başarı oranına sahiptir ve yanlış kategorize edilen bir haberi içerdiği sözcükler aracılığıyla ayırt edebilmektedir.<br/> 
Kısa metinli haberlerde  % 80 - %85 oranında başarı sağlamaktadır;haber başlıklarında ise %85 başarı oranına sahip.<br/> 
Başarılı örneklere [buradan](https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/tree/master/HaberGruplandirmaProgrami/images) bakabilirsiniz
# Sınıflar ve İçeriği<br/>
  
 Sınıf | Sınıf İçeriği
------------ | -------------
Spor | Spor ile ilgili tüm haberleri kapsar.
Politika | Türkiye ve Dünyada ki iç ve dış politikaları içerir.
Ekonomi | Türkiye ve Dünyada ki borsa,faiz,kriz vb alanlarını kapsar
Çevre |Türkiye ve Dünyada Ülkelerinde ; İl ve ilçelerdeki çevre ile ilgili haberleri kapsar
Dünya| Dünya haberlerini kapsar (Dünyadaki sağlık ,ölüm yaşam,ekonomi,politika,çevre  alanlarını  kapsamaz!!)
İşçi-Sendika| Türkiyedeki işçi ve sendika olaylarını kapsar
Bölge|Türkiye ve Coğrafya olarak yakın ülkeler ile ilgili olan konuları kapsar(ör: Libya,Suriye,Rusya...)
Medya|Sosyal medya ile ilgili haberleri ve ayrıca gazete,televizyon ile ilgili haberleri içerir.
Yaşam|Yaşam haberleri sağlık,yaşama dair olaylar ve ölüm haberlerini içerir(ör:Korona virüsü bu alana dahildir)

# Modelin Kurulum ve Kullanımı 
Öncelikle bu dizindeki tüm dosyaları indirin ve bir klasöre çıkartın.Daha sonra import etmeniz gereken kütüphaneleri hızlıca import edin.
Burada bulunan tüm sınıfları import etmeniz gerekiyor.<br/>
import  numpy , cv2 , sklearn, matplotlib, gensim ,nltk (bu sınıflar sizde yoksa indirmeniz gerekiyor)<br/>


eğer nltk kütüphanesini ilk kez import ediyorsanız nltk.dowload demeniz programın çalışması için gereklidir böylece nltk kütüphanesindeki verileri indirmiş olacaksınız<br/>
->> import nltk<br/>
->> nltk.download()<br/> komutunu yazıp programı çalıştırdığında  indirebilirsiniz.<br/>
Bunları kurduktan sonra haber_gruplandırıcı.py dosyasını açın ve çalıştırın ve kullanıma hazır hale gelecektir Programının kullanımını daha detaylı anlatımı aşağıdaki linkte video halindedir <br/>
[Haber Gruplandırıcı Tanıtım Videosu](https://www.youtube.com/watch?v=cqCNIBmJ14o)<br/>
# Kendime Özgü Buna Benzer Bir Programı Nasıl Kodlayabilirim
- Öncelikle kendinize çalışmak istediğniz  alan ile ilgili corpus hazırlamanız gerekiyor.(Detayli bilgi---> [Corpus Hazırlama](https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/tree/master/Corpus_Olusturma))
-Daha sonra oluşturacağınız modeli word2vec_model_olusturma.py dosyasını açarak open("dosya adı.txt",'r') olan kısma corpusunuzun adını yazıp çalıştırabilirniz.
-Oluşan modelinizi anahtar kelimeler oluşturup for döngüsü içerisinde sınıflandırma yapacağınız text içerisinde bulunan her kelimeyle üzerinden geçmeniz gerekiyor. <br/>
<img src="https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/blob/master/HaberGruplandirmaProgrami/tan%C4%B1t%C4%B1m.png"> <br/>
-Sınıflandırmada metin düzenleme ve kelime düzenleme işlemlerine dikkat etmeniz gerekli eğer iyi bir sınıflandırıcı yapmak istiyosanız Özel isimlerden ('nin 'nün vb..) eklerin çıkartılması ve gelen metindeki ile,gibi,ama gibi gereksiz ve sınıflandırmada programınızın kafasını karıştıracak sözcüklerin çıkartılması gerekir.Bu yüzden gelen veriden bunları çıkartıyoruz haber_aktarma.py dosyası bu işi bizim için yapıyor.

# Kaynaklar ve NLP için Nasıl bir katkı sağlandı
- İlk olarak yapay sinir ağları oluşturmadan yapay zeka kullanmadan sınıflandırma yapabildik ve başarısı yapay sinir ağı  ile yarışabilir durumda.(Doğal Sinir Ağı geliştirdik)
- İkinci olarak kök bulma, morfolojik inceleme ve kelime frekanslarını içeren kelime sayısı toplam 1 milyon 338 bin kelimeden oluşan text ile kök bulmaya, morfolojik incelemeye olanak sağladık.
- 13 bin  turizim haberi,800 turizim ile ilgili makaleden faydalanarak 1.5 milyon kelimeden oluşan türk gezi corpusundan faydalanarak trevel.model geliştirdik [Gezi.modelleri](https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/tree/master/gezi_model)
- Noktalama işaretlerini metinden kaldırma ve Corpusu kök kelimelerden oluşturmak için corpus_düzenleme.py kodları yazıldı.

# Sıkça Sorulan Sorular(SSS)
Algoritma Yeni mi?<br/>
- Bildiğiniz üzere yapay zeka alanı yapay sinir ağları üzerinde yoğunlaşmış durumda bizim kurduğumuz ise kelimelerden oluşan doğal bir sinir ağı daha önce eşine rastlamadım algoritmanın.<br/>





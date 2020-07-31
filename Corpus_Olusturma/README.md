# Corpus Olusturma
-Corpus nasıl olusturulur ve nelere dikkat edilir

# Corpus oluşturulurken nelere dikkat edilir<br/>
-Öncelikle corpusunuzun konusunun seçtiğiniz metinle ilgili olması büyük önem arz etmekte(örnek vermek gerekirse spor ile ilgiili bir proje yapıyosanız spor hakkında bilgilerin olması gerekiyor)<br/>
-İkinci olarak özel isimlere dikkat edilmeli.Fenerbahçe,Galatasaray gibi takımların isimleri özel olduğu için genellikle kesme işaretleriyle kullanılıyor bu yüzden korpusunuzda Fenerbahçe kelimesinin geçmesi yada bir olayın 
Fenerbahçe ile alakasını ölçmek istediğinizde hatayla karşılaşabilirsiniz bundan dolayı corpus_duzenleme.py dosyasını sizinle paylaştım eğer Türk Dili'nin doğru kullanımı veya çeviri  hakkında bir proje yapmıyorsanız bu programı kullanmanız yararınıza olacaktır.<br/>
-Bir diğer önemli husus oluşurduğunuz korpusun vektör uzunluğudur.Vectör uzunluğu korpusunuzda 1 kerede kaç kelime alıcağınızı belirler.Bundan dolayı spor ile ilgili bir proje hazırlarken metinlerinizi parçalara ayırmanız yararınıza olacaktır.
(örnek vermek gerekirse diyelimki elinizde  spor ile ilgili makaleler var , makalelerinizi bir işaretle birbirinden ayırırsanız bu makaleden maksimum verim elde edersiniz ?Makale giriş ?Makale gelişme ?Makale sonuç burda makalemiz 300 kelimeden oluşuyosa 100 kelimede bir ? işaretini kullandık ve 
corpusdan model  oluşturuken bu bize kolaylık sağlayacak.<br/>
# Kendi corpusumu nasıl oluşturabilirim
Kendi corpusunuzu oluşturmak için Request ve BeautifulSoup kütüphanelerinden yararlanmanız gerekiyor biraz html bilgilisi ve gözlem yeteneğinizi kullanarak projenize özel bir corpus oluşturabilirsiniz<br/>
Request ve BeautifulSoup kütüphanelerinin kullanımını bilmiyorsanız Aşağıda faydalı linkler bölümünde bulabilirsiniz 

Kolaylık olsun diye sizlere yukarıda 2 örnek bıraktım 
gezi_web_siteleri.py ve turk_gezi_corpus örneklerinden faydalanabilirsiniz.<br/> 
gezi_web.siteleri. py web sitesi adreslerini topluyor turk_gezi_corpus.py ise bu toplanan linklere girip corpus oluşmasını sağlıyor<br/> 
Deneme yapmak için önce gezi_web_siteleri.py yı çalıştırın daha sonra turk_gezi_corpus.py yi çalıştırın en sonunda da corpus_duzenleme.py dosyasını çalıştırın <br/> 



**Arkadaşlar bir konuya açıklık getirmek istiyorum . Her bir internet sitesinin kendi dinamikleri vardır bu yüzden bir kodu tüm internet sitelerinden bilgi çekmek için kullanamazsınız bilgileri almak için gözlem yapmanız ve örneklere bakmanız büyük önem arz ediyor.**<br/>

*Serinin sevilmesi ve yıldızların artması durumunda youtube videoları ve yeni örnekler bu kısımda paylaşıma açılacaktır takipte kalabilirsiniz. Umarım faydalı olabilmişimdir hepinize sağlıklı günler diliyorum.* <br/>

# Hazır Corpus ve Model Faydalı Linkler
[Hürriyet Gazetesi](https://github.com/hurriyet/developers.hurriyet.com.tr)<br/>
[Glove 6milyon kelime vektörü](https://nlp.stanford.edu/projects/glove/)

# BeautifulSoup ve Request ile internetten bilgi çekme Faydalı linkler
[İnternetten Veri Çekme](https://www.youtube.com/watch?v=00bc9BdUPSw&t=77s)<br/>
[İnternetten Veri Çekme](https://www.youtube.com/watch?v=WthFJcmGLhY&t=207s)<br/>
[Yazılım bilimi Github Adresi](https://github.com/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama)<br/>



# Corpus Düzenleme Nedir? Amacı nedir?
 Corpus düzenlemenin amacı modelin özel adları ve kelimeleri daha iyi tanıması için yapılmıştır özellikle küçük korpuslarda modelin  işlevini yükseltmek ,performansını artırmak için kullanılır.
 # Corpus Düzenleme Nasıl Çalışır ve Neler İçerir 
 -Özel adlardan ( ' " )  gibi kesme işaretlerinin ve kelime sonundaki noktalama işaretlerini kaldırır
 Örneğin ` Fenerbahçe'nin kelimesini Fenerbahçe olarak ; cümlede (yaptı. geldi,) gibi kelimeleri (yaptı geldi) olarak dönderir. "Halil GÜNBULAK' a "  olan ifadeyi Halil GÜNBULAK` olarak bizim için yeni bir text dosyasına yazar. Bunu tüm metindeki kelimeler için uygular.
 # Nasıl kurabilirim 
 open("file name","r",encoding='utf8') olan kısma kendi corpusunuzun bilgisayardaki adresini yazın ve corpus_duzenleme.py yı çalıştırın korpusunuz aynı dizinde corpus_düzenli.txt  olarak son hali çıkartilacaktır.<br/>
 *Coprusunuzu iki türlü düzenleyebilirsiniz*<br/> 
- Sadece noktalama işaretlerinin kaldırılması <br/>
- 1.seçenek + engelleyici kelimelerin (yani,gibi,ama..vb..) kaldırılması<br/>

2. seçeneğin yapımı için 

*c=open('corpusson.txt','r',encoding='utf8')<br/>
f=open('corpusduzenli2.txt','a',encoding='utf8')<br/>
text=c.read()<br/>
text=text.split()*<br/>
---> `text=haber.haberdüzenleme(text)` <---dizine bunu eklemeniz yeterli<br/>

# Referanslar
-Kendi oluşturduğumuz kelime kök ve morfolojik inceleme [Kelime İnceleme]( )

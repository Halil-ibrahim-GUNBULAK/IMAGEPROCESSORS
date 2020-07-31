# Kelime kökünü bulma ve morlojik yönden inceleme nedir?
Bildiğiniz gibi türkçede binlerce kelime ve bu kelimelerin çekimleri bulunmakta Bu projenin amacı hem kök bulmayı hemde kelimeleri tür bakımından incelemeye yönelik <br/>
Datasetimiz 1 milyon 330 bin türkçe kelimeyi  destekliyor.<br/>
## Nasıl Kurabilirim ?<br/>
-Zip dosyasını indirmeniz yeterli <br/>
## İçeriği ve Kullanımı <br/>
kelimekokubulma.py dosyası kendisine verilen kelimenin kökünü bulup size dönderir; aynı zamanda cümle verdiğinizde cümlede bulunan kelime köklerinin listesini size return eder.<br/>
<br/>
`---> from kelimekokubulma import kokbulma`<br/>
`---> s=kokbulma.kelime("merhabalar")`<br/>
`---> print(s)` <br/>
*-----------------Çıktısı---------------*<br/>
merhaba<br/>
<br/>
<br/>
`---> d=kokbulma.cumle("merhabalar bu programı böyle kullanabilirsiniz")`<br/>
`---> print(d)` <br/>
*-----------------Çıktısı----------------*<br/>
['merhaba', 'bu', 'program', 'böyle', 'kullan']
<br/>
<br/><<<<<<<<<<<<<<<<<<<<<<<<<----------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><br/>

kelimeturbulma.py dosyası kendisine gönderilen kelimenin ('Fiil','İsim','Sıfat','Zarf','Edat','Bağlaç','Zamir')hangi türde olduğunu size dönderir(Fiilimsiler dahil olmadığı için tüm fiilimsileri Fiil olarak dönderiyor)<br/>
<br/>
---> `from kelimeturbulma import morfoloji`<br/>
---> `s=morfoloji.kelimeturu("merhabalar")`<br/>
---> `print(s)` <br/>
*-----------------Çıktısı---------------*<br/>
İsim<br/>
<br/><br/>

---> `d=kokbulma.cumle("buraya bir metin giriyoruz ve bu metinin morfolojik olarak sırayla gösteriyor")`<br/>
---> `print(d) `<br/>
*-----------------Çıktısı---------------*<br/>
['İsim', 'bulunamadı', 'İsim', 'Fiil', 'Bağlaç', 'bulunamadı', 'İsim', 'Sıfat', 'Fiil', 'İsim', 'Fiil']<br/>
<br/><br/>
<br/>
- Listede olmayan kelimeleri bulunamadı olarak dönderidi <br/>

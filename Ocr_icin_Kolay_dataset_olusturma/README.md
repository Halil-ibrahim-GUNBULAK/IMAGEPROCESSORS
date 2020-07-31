# Data Set Özellikleri
- 28x28 boyutunda yaklaşık 120 bin resim bulunduruyor<br/>

- A-Z türkçe karakterilerinide içeriyor.<br/>

- Bazı kendisi ve küçük harfı benzeyen büyük harfler datasetinden daha iyi tanımlama yapılması için kaldırılmıştır(Örnek=O o,Ö ö,J j)<br/>

- Data seti 28x28 boyutundan oluşan toplamda 120 bin resim bulunduruyor bunu oluşturmak için önce exel dosyası hazırladık ve gerekli harfleri yazdık daha sonra exel dosyasında satır ve sutun genişliklerini 28 piksel olarak değiştirdik.<br/>
<img src="https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/blob/master/Ocr_icin_Kolay_dataset_olusturma/uu%20(2).png" width="28" height="28"><img src="https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/blob/master/Ocr_icin_Kolay_dataset_olusturma/yb%20(2).png" width="28" height="28"><br/>
<img src="https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/blob/master/Ocr_icin_Kolay_dataset_olusturma/1%20(3).png" width="28" height="28"><img src="https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/blob/master/Ocr_icin_Kolay_dataset_olusturma/2%20(0).png" width="28" height="28">


Böylelikle ekran görüntüsü aldığımızda yazdığımız kod resmin herbir 28 piksel genişlikte üzerinde geziniyor ve yeni bir resim şeklinde bizler için open cv kütüphanesini kullanarak oluşturuyor.

Oluşturulan resimlerden 1 tane test klasörüne 1 tane train klasörüne atıyoruz görüntü işlemede kullanılacak resimler genelde 1 test 5 train
oranında olmalı hem bundan dolayı hemde resimlerin büyüklüklerini ve farklı açılardan görünümü sağlamak için cv2.resize ile resmi %110, %120, %130, %140 oranında büyütülmüş şekilde train klasörüne attık Hem bizden istenen 1/5 oranını sağladık hemde data setimizde daha büyük görünen harflerin olmasını sağladık.

# Türk Alfabe data seti oluşturma
- Data setini oluşturmak için önce dosyayı bütün halinde indirin
- İnen zip dosyasını klasöre çıkartın ve res-kirpma-test.py dosyasını açın
- `*Tüm cv2.imwrite("C:/tensorflow1/models/research/object_detection/kerasimage/train/"...)` kısımlarını indirdiğiniz klasör adresi olarak değiştirin ... yani devamı olan kısmı silmeyin
- İnen klasördeki train ve test klasörünün içlerinde bulunan resimleri silin. 
- Son olarak `res-kirpma-test.py` dosyasını çalıştırın
## *Kendinize özgü bir data seti yapmak isterseniz harfler.xlsx ve harfler2.xlsx dosyalarının ekran görüntüsünü alıp tam 28 in katları olacak şekilde ayarlamanız ve klasörün içine test1.png olarak kaydetmeniz yeterli.*
<img src="https://github.com/Halil-ibrahim-GUNBULAK/IMAGEPROCESSORS/blob/master/Ocr_icin_Kolay_dataset_olusturma/test1.png" width="720" height="480">




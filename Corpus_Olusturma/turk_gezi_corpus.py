import requests
from bs4 import BeautifulSoup

f=open('turklink.txt','r',encoding='utf8') # linkleri okuyacağımız  dosyayı açtık
text=f.read()
textslist=text.split('\n')
d=open('turkcorpus.txt','a',encoding='utf8') #Linklerin corpus halini oluşturacağımız dosyayı açtık a kullanma sebebimiz yeni satıra geçip alttan devam etmesi w yaparsanız eski yazdığınız satırı siler

for c in range(len(textslist)):
   try:
     link=textslist[c]

     r=requests.get(link) # linki text ten aldık ve request ile istek gönderdik
     soup=BeautifulSoup(r.content)
     # Bu kısımdan sonrası tüm siteler için değişiyor  site sayfa kaynağı ile ilgili göslem yapmak için print(soup.prettify()) kullanmanız yararınıza olur
     print(soup.prettify())
     metalar=soup.find_all('p')#ben metinlerin <p> arasında olduğunu gördüm bu yüzden dolayısoup.find_all kısmına "p" yazdım bu daha öncede dediğim giib siteden siteye değişiyor

     d.write('*')
     min=0
     max=0
     counter=0 #Sitede istediğimiz yazılar angle ve  Türkiye'den ve Dünya’dan son dakika haberleri, köşe yazıları arasında bulunduğunu keşfettim bu yüzden bu kelime ve cümle arasındaki herşeyi aldım
     a="Türkiye'den ve Dünya’dan son dakika haberleri, köşe yazıları"
     print(len(a))
     for i in range(0,len(metalar)):

         str_s=str(metalar[i])

         if str_s[48:53]=='angle':
          min=i;
         if str_s[23:83]==a:
           max=i

         #print(metalar[i])
     # son olarak min ve max i belirledik sitedeki bilgilerin kullanılması yasak olduğu için korpus paylaşmadım ama çok daha büyük 50 mb lık turizim haberlerinden
     # ve türkiye turizim ile ilgili hazırlanmış  3 milyon kelime üzerinde eğitilmiş bir modeli paylaştım onu indirip kullanabilirsiniz

     for i in range(min+1,max):

        d.write(str(metalar[i])+'\n')
     print(max,min+1)
   except BaseException:
    print("link geçersiz")




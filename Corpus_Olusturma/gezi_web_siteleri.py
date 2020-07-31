import requests
from bs4 import BeautifulSoup
linklertoplam=[]
# öncelikle haber sitesinin page şeklinde olması önemli
# burda linkleri alıp link listesi oluşturuyoruz
#html bilenler bilir a href kısmında bizim linklerimiz bulunmakta fakat sitedeki her link işimize yaramıyor
# bu yüzden öncelikle göslem yapmanız geriyor ben yaptığım gözlemle birlikte işimize yarayan linkler
#https://play.google.com/store/apps/details?id=hurriyet.mobil.android&hl=tr && /seyahat/konu/gezgin/?p= linkleri arasında olduğunu keşfettim
# bu yüzden buna uygun bir kod ile linkeri aldım
# oluşan korpusunu düzenlemeniz için korpus düzenleme py de bırakıyorum bu metninizdeki noktalama işaretlerini kaldıracak bir program örnek vermek gerekirse
# Fenerbahçe'nin takım otobüsü. cümlesini size Fenerbahçe takım otobüsü olarak dönderecek bu da size Fenerbahçe ve otobüsü kelimesini kazandıracak
# diğer türlü modelinizin bu kelimeleri tanıması için çokca otobüsü. ve Fenerbahçe'nin kelimelerinin çokca geçmesi gerekir bu şekilde özel isimler ve noktalama işaretlerinden kurtuluyoruz
for p in range(2,49):
  r=requests.get("https://www.hurriyet.com.tr/seyahat/konu/gezgin/".format(p))

  soup=BeautifulSoup(r.content)

  linkler=soup.find_all("a")
  linklist=[]

  list_min=0
  list_max=0
  counter=0
  counter2=1
  for link in linkler:
    s=link.get("href")
    linklist.append(s)
    counter=counter+1
    str_s=str(s)

    if  str_s[:]=="https://play.google.com/store/apps/details?id=hurriyet.mobil.android&hl=tr":
        print(counter)
        list_min = counter
    if str_s[0:24]=='/seyahat/konu/gezgin/?p=' and counter2==1:
        counter2=counter2+1
        print(counter)
        list_max = counter




  for i in range(list_min,list_max-1):
       linklertoplam.append(linklist[i])

  print(len(linklertoplam))

  dosya= open('turklink.txt', 'a', encoding='utf8')

  for d in range(len(linklertoplam)):
      dosya.write('https://www.hurriyet.com.tr'+str(linklertoplam[d])+'\n')




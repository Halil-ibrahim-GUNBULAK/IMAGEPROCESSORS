from kelimekokubulma import kokbulma
#eksik yanı fiilimsi özelliğinin olmaması
#fiilimsi yapılmak isteniyorsa  kelime kökünden değil kelimeden ilerleyip
# kelimenin ilk ve ikinci  tarafı (ex:Fiil + Mastar) alınıp yapılabilir geliştirilmesi gereken konu olarak kalsın
t = open('kelimemorf.txt', 'r', encoding='utf8')
text = t.read()
morf_list = text.split('\n')


class morfoloji:
    def turler(a):
     turlist=['Fiil','İsim','Sıfat','Zarf','Edat','Bağlaç','Zamir']
     for i in  range(len(turlist)):
         if a==turlist[i]:
            return turlist[i]
     return  'Lütfen bu seçimlerden birini yapınız Fiil, İsim,Sıfat,Zarf,Edat,Bağlaç,Zamir'


    def kelimeturu(a):
            kelimemiz=kokbulma.kelime(a)


            b = 'bulunamadı'
            for i in range(len(morf_list)):

                if morf_list[i] == kelimemiz:

                    c= morf_list[i + 1]
                    if c[0:4]=='Verb':
                        b='Fiil'
                    elif c[0:4]=='Noun':
                        b='İsim'
                    elif c[0:4] == 'adj':
                        b ='Sıfat'
                    elif c[0:4] == 'adv':
                        b ='Zarf'
                    elif c[0:4] == 'Post':
                        b ='Edat'
                    elif c[0:4] == 'conj':
                        b ='Bağlaç'
                    elif c[0:4] == 'Pron':
                         b='Zamir'
                    return b

            return b
    def cumleturu(a):
        cumle_turu = []
        kellis = a.split(' ')
        for k in range(len(kellis)):
            cumle_turu.append(morfoloji.kelimeturu(kellis[k]))

        return cumle_turu

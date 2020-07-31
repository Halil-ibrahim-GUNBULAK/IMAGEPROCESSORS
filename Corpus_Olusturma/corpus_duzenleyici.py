#düzenlemek istediğiniz dosyanın ismini r kısmına giriniz
c = open('turkcorpus.txt', 'r', encoding='utf8')
# dosyayı düzenli halde size vermesini istediğiniz ismi veriniz
f = open('corpusduzenli.txt', 'a', encoding='utf8')
text = c.read()
text = text.split()

class metinDuzenle:


    def corpusDuzenleme(text):
        metinText = []
        test = ''
        # metindeki kelimeleri aldık
        for i in range(len(text)):
            # kelimelerdeki harfleri aldık
            a = len(metinText)
            src=text[i][0:4]
            if text[i][0:4] == "src=" or text[i][0:4]=="<spa":
                text[i]=''
            print((i/len(text))*100)
            for k in range(len(text[i])):

                if text[i][k] == "'"  or text[i][k] == '’' or text[i][k] == "." or text[i][k] == '”' or text[i][k] == ","  or text[i][k] == ':' or \
                        text[i][k] == ';' or  text[i][k] == '>' :
                    metinText.append(text[i][0:k])
                    test = test + str(text[i][0:k])+' '
                    # burdaki algoritma biz zaten gelen kelime uzunluğunu biliyoruz “ işarete raslayınca onu atlayıp geri kalan kelimeyi alıyoruz
                if text[i][k] == "“" or  text[i][k] == '<':
                    metinText.append((text[i][1:len(text[i])]))
                    test=test+(str(text[i][1:len(text[i])]))+' '
                # zor olan kısmı " için yapmak  cünkü kelimenin başındamı sonundamı karar vermesi gereken bilgisayar olucak
                # mesela "kelime......kelime" iki şekildede olabilir bu yüzden bir sonraki harf len(text[i]) içindeyse başta
                # dışındaysa sonda olduğunu anlayıp buna göre yazıcaz k+1 kullandık çünkü k range(0 dan 7 )ye diyelim k en fazla 6 oluyor
                if text[i][k] == '"' and k + 1 < len(text[i]):
                    metinText.append((text[i][1:len(text[i])]))
                    test = test + str((text[i][1:len(text[i])]))+' '
                elif text[i][k] == '"' and k + 1 == len(text[i]):
                    metinText.append((text[i][0:k]))
                    test=test+str(text[i][0:k])+' '

            if a == len(metinText):
                metinText.append(text[i])
                test = test + str(text[i])+' '
        return test

    f.write(corpusDuzenleme(text))

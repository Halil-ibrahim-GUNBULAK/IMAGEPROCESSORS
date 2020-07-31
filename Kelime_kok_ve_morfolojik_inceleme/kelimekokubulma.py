f = open('kelimeler.txt', 'r', encoding='utf8')
text = f.read()
t_list = text.split('\n')
print("kök ve kelimeler listeye atandı")
r = open('kelimekokleri.txt', 'r', encoding='utf8')
text = r.read()
kokler_list = text.split('\n')
class kokbulma:

    def kelime(a):

        for i in range(len(t_list)):
          if a==t_list[i]:
            try:
             kok=kokler_list[2*i+1]
             return kok
            except IndexError:
             return a
        return a


    def cumle(a):


        kokcumle=[]
        kellis=a.split(' ')
        for k in range(len(kellis)):
             kokcumle.append(kokbulma.kelime(kellis[k]))


        return kokcumle



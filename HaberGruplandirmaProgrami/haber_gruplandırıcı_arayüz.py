from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import*
import sys
import cv2
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from kelimekokubulma import kokbulma
from kelimeturbulma import morfoloji
from haber_aktarma import haber
from matplotlib import pyplot as plt
import numpy as np
from Haber_gruplandırma_ana_prog import*
from Haber_gruplandırma_ana_prog import habersiniflandirma

class HaberWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 50, 700, 1000)
        self.setWindowTitle("Haber Sınıflandırma")
        self.UI()

    def UI(self):

        self.grafik = QLabel(self)
        self.grafik.setGeometry(100,100,800, 500)
        self.grafik.move(200,500)

        self.label=QLabel(self)
        self.label.setText("SONUÇ=")
        self.label.move(0,500)

        self.line = QLineEdit(self)
        self.line.move(50,500)
        self.haber=QTextEdit(self)
        self.haber.move(200,0)
        self.haber.setGeometry(0,0,500,500)




        self.resim=QLabel(self)
        self.resim.setPixmap(QtGui.QPixmap("simge.png"))
        self.resim.setGeometry(0,0,200,200)
        self.resim.move(500,0)

        self.buton1 = QPushButton(self)
        self.buton1.setGeometry(0, 0,200,200)
        self.buton1.move(500,200)
        self.buton1.setText("Haber Türünü Bul")

        self.buton1.clicked.connect(self.click)





        self.show()

    def click(self):

        text=self.haber.toPlainText()
        text = text.split()
        text = haber.haberduzenleme(text)
        text = haber.metinDuzenleme(text)
        textBoyutu = len(text)

        a =habersiniflandirma.metin(text)
        print(a)
        s=habersiniflandirma.sonucu_goster(a)
        self.line.setText(s)
        self.grafik.setPixmap(QtGui.QPixmap("hi.png"))




if __name__== "__main__":
    app=QApplication(sys.argv)
    win=HaberWindows()
    sys.exit(app.exec_())


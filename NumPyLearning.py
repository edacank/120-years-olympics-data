import numpy as np

dizi = np.array([1,2,3,4,5,6,7])
print(dizi)
print(dizi.shape)
print("şekil: ", dizi.shape)
print("boyut:", dizi.ndim)
print("veritipi: ", dizi.dtype.name)
print("boy : ", dizi.size)
print("type: ", type(dizi))
#dizinin 1. elemanı yani sıfırıncı indeksteki eleman
print(dizi[0])
#dizinin ilk 4 elemanı
print(dizi[0:4])
#dizinin tersi
print(dizi[::-1])
#matrislerde indeksleri ve dilimleri incelemek için 2 boyutlu bir matris oluşturalım
dizi2D= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)
#dizinin birinci satır ve sütununda bulunan elemanı
print(dizi2D[1,1])
#dizinin 1. sütununun tüm satırları
print(dizi2D[:, 1])
#dizinin 1. satırının 1. 2. 3. elemanı
print(dizi2D[1, 1:4])
#dizinin son satırının yani 2. satırın tüm sütunları
print(dizi2D[-1,:])
#dizinin son sütununun tüm satırları
print(dizi2D[:,-1])
#ŞEKİL MANİPÜLASYONU
dizi_2D = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(dizi_2D)
#VEKTÖR HALİNE GETİRME: ravel: düğüm çözmek, tel tel hale getirmek
vektor = dizi_2D.ravel()
print(vektor)
#reshape
vektor.reshape(3,3)
#transpoze
print(dizi_2D.T)
#DİZİLERİN İSTİFLENMESİ: stack --> vertical stack and horizontal stack
dizi1 = np.array([[1, 2], [3, 4]])
print(dizi1)
dizi2= np.array([[-1, -2],[-3, -4]])
print(dizi2)
#iki diziyi alt alta ekle: sütun sayısı sabit satırları artırır
dizi_dikey = np.vstack((dizi1, dizi2))
print(dizi_dikey)
#iki diziyi yan yana ekle: satır sayısı sabit sütunları artırır.
dizi_satır= np.hstack((dizi1,dizi2))
print(dizi_satır)



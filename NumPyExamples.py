import numpy as np
array_range = np.arange(10, 50, 5)
print(array_range)
array_range = np.arange(10, 10000, 5**2)
print(array_range)
array_space = np.linspace(10, 20, 5)
print(array_space)
dizi2D = np.array([[1,2,3,4],[6,7,8,9]])
print(dizi2D)
#dizinin 1. satır ve 1. sütunda bulunan elemanı
print(dizi2D[1,1])
#dizinin 1. sütunun tüm satırları
print(dizi2D[:,1])
#dizinin 1. satırının 1. 2. 3. elemanı
print(dizi2D[1, 1:4])
#dizinin son satırının tüm sütunları
print(dizi2D[-1,:])
#dizinin son sütununun tüm satırları
print(dizi2D[:,-1])
#ŞEKİL MANİPÜLASYONU VE DİZİLERİ İSTİFLEME
vektor=dizi2D.ravel()
print(vektor)
vektor1=vektor.reshape(2,4)
print(vektor1)
vektor1=vektor.reshape(4,2)
print(vektor1)
dizi_reshaped = np.resize(dizi2D,(4,4))
print(dizi_reshaped)
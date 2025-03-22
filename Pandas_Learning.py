import pandas as pd
#pandas veri çerçevesi oluşturmak için önce sözlük oluşturmak gerekli
dictionary = {"isim": ["ali", "veli","kenan","cemile","ayse","cemre","atilla","meltem"],
              "yas": [15,14,17,19,23,24,34,43],
              "maas": [1000,1500,3000,2300,5670,1000,3000,3000]}
veri = pd.DataFrame(dictionary)
print(veri)
#verinin ilk 5 satırına bakmak için
print(veri.head()) #veri ile ilgili ilk izlenimi elde etmek için
#verinin son beş satırı
print(veri.tail())
#verinin sütunları
print(veri.columns)
#bilgi alma
print(veri.info())
#veri ile ilgili istatiksel değerleri görmek için kullanılacak metot
print(veri.describe())
#verinin bir sütununu çağırmak için
print(veri["yas"])
#veriye yeni bir sütun eklemek için
veri["şehir"]= ["adana","amasya","ankara","ardahan","aydın","adıyaman","antalya","bursa"]
print(veri)
#verinin yaş sütununu başka bir yöntemle alalım
print(veri.loc[:,"yas"])
#yas sütununu ve indeksi 3e kadar olan satırları al. not: 3 dahil
print(veri.loc[:3,"yas"])
#indeksi 3e kadar olan satırları ve yastan sehire kadar olan sütunları al
print(veri.loc[:3,"yas":"şehir"])
#indeksi 3d kadar olan satırlar ile yaş ve isim sütunlarını al
print(veri.loc[:3, ["isim","yas"]])
#satırları tersten yazma
print(veri.loc[::-1,:])
#yas sütununu iloc ile yazdır. yas sütun listesinde 1 nolu indekse sahip
print(veri.iloc[:,1])
#ilk satırı ve yas ve isim sütunlarını al iloc ile
print(veri.iloc[:3,[0,1]])
#FİLTRELEME
#ilk olarak yasa göre bir filtreleme oluşturalım yas>22
filtre1 = veri.yas>22
filtrelenmis_veri= veri[filtre1]
print(filtrelenmis_veri)
#şimdi de yası 22 den büyük olup şehri antalya olan örnekleri bulalım
filtre2= veri.şehir == "antalya"
print(veri[filtre1 & filtre2])
#LİSTE KAVRAMA
#yas ortalaması
#not: numpy ile de yazılabilirdi. np.mean(veri.yas)
ortalama_yas= veri.yas.mean()
print(ortalama_yas)
veri["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)
#küçük harfe çevirme
veri.columns = [i.lower() for i in veri.columns]
print(veri)
# liste kavrama yöntemi yerine lambda fonksiyonunu kullanabiliriz.
veri = veri.assign(yas_5_yil_sonra=lambda x: (x['yas']+5))
print(veri)
#apply metodunu da liste kavrama yöntemi yerine kullanabiliriz.
def YasOnYilSonra(age):
    return age + 10
veri["yas_10_yil_sonra"] = veri.yas.apply(YasOnYilSonra)
print(veri)
#BİRLEŞTİRME
#veri seti 1 i oluşturalım
sozluk1 = {"isim":["alina","belinay","sedat"],
           "yas": [13,14,19],
           "sehir": ["izmir","adana","kastamonu"]}
veri1 = pd.DataFrame(sozluk1)
print(veri1)
#veri seri 2yi oluşturalim
sozluk2 = {"isim": ["pelinsu","memoli","deniz"],
           "yas": [12,14,20],
           "sehir": ["zonguldak","mardin","ordu"]}
veri2= pd.DataFrame(sozluk2)
print(veri2)
#dikey birleştirme; axis = 0 ise dikey
veri_dikey = pd.concat([veri1,veri2],axis=0)
print(veri_dikey)
#yatay birleştirme; axis=1 ise yatay
veri_yatay= pd.concat([veri1,veri2],axis=1)
print(veri_yatay)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
#uyarıları kapat
import warnings
warnings.filterwarnings("ignore")
veri = pd.read_csv("athlete_events.csv")
print(veri.head())
print(veri.info())
#sütun isimlerini düzeltme/Türkçeleştirme
print(veri.columns)
#rename
veri.rename(columns={
    'ID': 'id',
    'Name': 'isim',
    'Sex': 'cinsiyet',
    'Age': 'yas',
    'Height': 'boy',
    'Weight': 'kilo',
    'Team': 'takım',
    'NOC': 'uok' ,
    'Games': 'oyunlar',
    'Year': 'yil',
    'Season': 'sezon',
    'City': 'sehir',
    'Sport': 'spor',
    'Event': 'etkinlik',
    'Medal': 'madalya'}, inplace = True)



print(veri.columns)
#drop metodu ile id ve oyunlar sütunlarını silelim
veri= veri.drop(["id","oyunlar"], axis=1)#axis=1 sütunları temsil eder
print(veri.columns)
print(veri.head(2))
#boy ve kilo sütununda bulunan layıp veriyi etkinlik ortalamasına göre dolduracağız
essiz_etkinlik= pd.unique(veri.etkinlik)
print("eşsiz etkinlik sayısı: {}".format(len(essiz_etkinlik)))
print(essiz_etkinlik[:10])

#her bir etkinliği iteratif olarak dolaş
#etkinlik özlinde boy ve kilo ortalamalarını bul
#etkinlik özelinde boy ve kiloda kayıp olan değerlere ortalama boy ve kilo değerlerini eşitle
veri_gecici= veri.copy() #gerçek veriyi kaybetmemek için kopya oluştur.
boy_kilo_liste = ["boy", "kilo"]
for e in essiz_etkinlik: #tkinlik listesi içind dolaş
    #etkinlik filtresi oluştur
    etkinlik_filtre  = veri_gecici.etkinlik == e
    #veriyi etkinliğe göre filtrele
    veri_filtreli = veri_gecici[etkinlik_filtre]

    #boy ve kilo için etkinlik özelinde ortalama hesapla
    for s in boy_kilo_liste:
        ortalama= np.round(np.mean(veri_filtreli[s]),2)
        if ~np.isnan(ortalama): #eğer etkinlik özelinde ortalama hesaplanabiliyorsa
            veri_filtreli[s] = veri_filtreli[s].fillna(ortalama)
        else: #eğer etkinlik özelinde ortalama hesaplanamıyorsa tüm veri için ortalamayı bul
            tum_veri_ortalamasi = np.round(np.mean(veri[s]),2)
            veri_filtreli[s] = veri_filtreli[s].fillna(tum_veri_ortalamasi)
    #etkinlik özelinde kayıp değerleri doldurulmuş olan veriyi veri_geicic değişkenine eşitle
    veri_gecici[etkinlik_filtre]= veri_filtreli
#kayıp değerleri giderilmiş geçici veriyi gerçek veri değişkenine eşitle
veri= veri_gecici.copy()
print(veri.info()) #boy ve kilo sütunlarında kayıp değer sayısna bak


#yaş sütununda bulunan kayıp veriyi veri setinin ortalamasına göre bulacağız
#yaş değişkeni tanımlı olmayan verileri bul
#tilda işareti ile tersini al
#yaş değişkeni tanımlı olan verileri bulmak için bir filtre oluştur
yas_ortalamasi = np.round(np.mean(veri.yas),2)
print("yaş ortalaması : {}".format(yas_ortalamasi))
veri["yas"]= veri["yas"].fillna(yas_ortalamasi)
print(veri.info())

#3 madalya alamayan sporcuları çıkart
#toplamda 231233 tane örnek içinmadalya değişkeni tanımlı değil
madalya_degiskeni= veri["madalya"]
print(pd.isnull(madalya_degiskeni).sum())

#madalya değişkeni tanımlı olmayan örnekleri bul (Nan)
#tilda ile tersini al
#madalya değişkeni olan örnekleri bulmak için filtre oluştur
madalya_degiskeni_filtresi = ~pd.isnull(madalya_degiskeni)
veri = veri[madalya_degiskeni_filtresi]
print(veri.head(5))
veri.to_csv("olimpiyatlar_temizlenmis.csv", index=False)
#TEK DEĞİŞKENLİ SAYISAL VERİ ANALİZİ
#öncelikle histogram grafiğini elde edeceğimiz metodumuzu yazalım
def plotHistogram(degisken):
    """

    girdi: değişken/sütun ismi
    çıktı: histogram grafiği

    """
    plt.figure()
    plt.hist(veri[degisken], bins=85, color="orange")
    plt.xlabel(degisken)
    plt.ylabel("frekans")
    plt.title("veri sıklığı-{}".format(degisken))
    plt.show()
#sayısal değişkenler için histogram çizdirelim
sayisal_degisken =["yas","boy","kilo","yil"]
for i in sayisal_degisken:
    plotHistogram(i)
print(veri.describe())

#YAŞ DEĞİŞKENİ İÇİN BOX PLOT KUTU GRAFİĞİ ÇİZDİRELİM.
#yaş değişkeni için filtreyi uygulayıp sonra kutu grafiği çizdirelim.
plt.boxplot(veri.yas)
plt.title("yaş değişkeni için kutu grafiği")
plt.xlabel("yaş")
plt.ylabel("değer")
plt.show()

#BAR GRAFİĞİ ELDE EDECEĞİMİZ METODUMUZU YAZALIM
def plotBar(degisken, n=5):
    """


    Girdi: değişken/sütun ismi
        n= en önemli beş eşsiz değer
    çıktı: bar grafiği

    """
    veri_ = veri[degisken]
    veri_sayma = veri_.value_counts()
    veri_sayma = veri_sayma[:n]
    plt.figure()
    plt.bar(veri_sayma.index, veri_sayma, color="purple")
    plt.xticks(veri_sayma.index, veri_sayma.index.values)
    plt.xticks(rotation=45)
    plt.ylabel("frekans")
    plt.title("veri sıklığı {} :".format(degisken))
    plt.show()
    print("{}: \n {}".format(degisken),veri_sayma)
    #sayısal değişkenler için histogram çizdirelim
    kategorik_degisken = ["isim","cinsiyet","takım","uok","sezon","sehir","spor","etkinlik","madalya"]
    for i in kategorik_degisken:
        plotBar(i)
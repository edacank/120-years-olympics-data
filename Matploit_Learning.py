import pandas as pd
veri = pd.read_csv("iris.csv")
print(veri.head())
print(veri.columns)
#veri içerisinde kaç adet unique değer var?
print(veri.variety.unique())
#veri ile ilgili bilgiler
print(veri.info())
print(veri.describe())


#çizgi grafiği yapımı
import matplotlib.pyplot as plt
plt.figure()
plt.plot(veri["variety"], veri['sepal.length'], color="pink", alpha = 0.7)
plt.title('alt yaprak uzunluğu')
plt.xlabel("id")
plt.ylabel("Cm")
plt.grid(True)
plt.show()

#saçılım grafiği yapımı
plt.figure()
plt.scatter(veri["sepal.length"],veri["sepal.width"], color="blue", s=15, alpha= 0.7)#alpha saydamlık s= size
plt.title('alt yaprak uzunluğu ve genişliği')
plt.xlabel("alt yaprak uzunluğu -cm")
plt.ylabel("alt yaprak genişliği- cm")
plt.grid(True)
plt.show()
#sepal length ve petal length sütunlarının histogramını çizdirelim
plt.figure()
plt.hist(veri["sepal.length"],color="green", alpha= 0.5, bins= 20, label="alt yaprak uzunluk")
plt.hist(veri["petal.length"],color="red", alpha= 0.5, bins =20, label= "üst yaprak uzunluk")
plt.title('alt yaprak ve üst yaprak uzunluğu histogram')
plt.xlabel=("cm")
plt.ylabel=("frekans")
plt.legend()
plt.show()

#çubuk grafiği
veri_sütun_listesi =['sepal.width','petal.length','petal.width']
tanım = veri.describe()
print(tanım)
#alt yaprak uzunluk ve genişlik, üst yaprak uzunluk ve genişlik ortalama değerlerini bulalım
ortalama = tanım.iloc[1, [1, 2, 3]]
print(ortalama)
plt.figure()
plt.bar(veri_sütun_listesi, ortalama)
plt.title('alt üst yaprak uzunluğu ve genişliği ortalama')
plt.ylabel=("cm")
plt.show()

#alt plan grafiği
fig, ax = plt.subplots(2,1) #figür üzerine 2*1lik bir tablo oluşturur. bu tablo üzersine ax eksen ekler
fig.suptitle("alt yaprak uzunluk ve üst yaprak uzunluk", fontsize=14)
ax[0].plot(veri["sepal.length"], veri["sepal.width"], color="purple", label="sepal.legnth-width")
ax[0].set_title('alt yaparak uzunluk')
ax[0].set_xlabel("sepal.length")
ax[0].set_ylabel("sepal.width")
ax[1].plot(veri["petal.length"], veri["petal.width"], color="yellow", label= "petal-")
ax[1].set_title('üst yaprak uzunluk')
ax[1].set_xlabel("1")
ax[1].set_ylabel("cm")
fig.tight_layout()
fig.subplots_adjust(top=0.85)
plt.show()


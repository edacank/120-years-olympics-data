def daireAlanıHesapla(r):
  """"
  daire alanını hesalamak için


  """
  pi = 3.14
  daire_alanı= pi*(r**2)
  return daire_alanı
daireAlanıHesapla(3)
print (daireAlanıHesapla(3))
def fonksiyonLambda(n):
  return lambda a: a * n
ana_fonksiyon = fonksiyonLambda(3)
ana_fonksiyon(5)
print(ana_fonksiyon(5))
sayı_listesi = [1,2,34,5,6]
sayı_listesi.remove(2)
print(sayı_listesi)
sayı_listesi.append(45)
print(sayı_listesi)
sayı_listesi.reverse()
print(sayı_listesi)
sayı_listesi.sort()
print(sayı_listesi)
#tuple veri tipi
tuple_veritipi = (1,2,99,4,5)
print(tuple_veritipi [4])
print(tuple_veritipi[:3])
print(tuple_veritipi[3:])
print(tuple_veritipi.count(99))
# sözlük veri tipi: karma tablo türüdür
dictionary = {"istanbul": 34, "izmir": 35,"konya":42}
print(dictionary)
print(dictionary['istanbul'])#istanbul anahtarının değeri
print(dictionary.keys()) #tüm anahtarları getirir.
print(dictionary.values()) #tüm değerleri getirir
#koşullu ifadeler
sayi1= 13
sayi2= 13
if sayi1<sayi2:
  print("sayi1 küçüktür sayi2")
elif sayi2<sayi1:
  print("sayi2 küçüktür sayi1")
else: print("sayi1 eşittir sayi2")
liste= [1,2,3,4,5,6,7,8,9]
deger =1
if deger in liste:
  print("{} değeri listenin içinde".format(deger))
else:
  print("{} değeri listenin içinde DEĞİL".format(deger))
#deger1 =dictionary['istanbul']
deger1 = 44
if deger1 in dictionary.values():
  print("{} değeri listenin içinde".format(deger1))
else:
  print("{} değeri listenin içinde değil...".format(deger1))

dictionary = {"türkiye":"ankara", "ingiltere":"londra","ispanya":"madrid"}
keys = dictionary.keys()
deger2= "türkiye"
if deger2 in keys:
  print("{} değeri sözlüğün içindedir.".format(deger2))
else:
  print("{} değeri sözlüğün içinde değildir.".format(deger2))
#for döngüsü
for i in range(2, 9):
  print(i)
for i in "ankara konya":
  print(i)
metin = "bursa adana"
metin_ayrik= metin.split()
print(metin_ayrik)

for i in metin_ayrik:
  print(i)
#for döngüsü ile toplama
liste_sayı = [1, 2, 3, 4, 5, 6]
count = 0
for c in liste_sayı:
  count = count+c
print(count)
print(sum(liste_sayı)+1)
#while döngüsü
i=0
while(i<4):
    print(i)
    i = i+1
list = [1,2,3,4,5,6]
sinir = len(list)
indis=1
toplam=0
while(indis<sinir):
  toplam= toplam+list[indis]
  indis = indis+1
print(toplam)


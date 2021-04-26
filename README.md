## Web İndeksleme Uygulaması



Proje detayları için : [Proje Raporu](https://github.com/sevkikaragol/webIndex/blob/main/rapor.pdf)

## Kurulum/Çalıştırma
Terminale
```
pip install flask
```
yazılarak öncelikle Flask kurulumu yapılmalıdır. Daha sonra terminalde proje klasörüne gelerek
```
python webIndex.py
```
yazarak localhost'unuzda projeyi çalıştırıp kullanıma başlayabilirsiniz. <br>

## Özet
Bu projede, projeyi yapan kişiler
için web tabanlı uygulamaların çalışma 
mantığını anlaması, bunun ardından web 
indeksleme yöntemleri hakkında bilgi edinilmesi ve web tabanlı uygulama yazma 
becerisinin geliştirilmesi amaçlanmaktadır. 
Bu amaç doğrultusunda öğrencilerden, bir 
web sitesinin frontend ve backend kısmının 
geliştirilmesi ve belli isterler doğrultusunda bu web sitesinin bir amaca hizmet etmesi istenmiştir. 
Bu amaçlar ve isterler doğrultusunda 
Python (Flask), HTML,CSS (Bootstrap) ve 
internet üzerinden veri çekmek için çeşitli 
kütüphaneler kullanılarak verilen URL’ler 
üzerinden proje isterlerini uygulayan bir 
web sitesi geliştirilmiş, test çalışmaları 
yapılmış ve kullanıma hazır hale getirilmiştir. Web sitesi çevrimiçi yayına alınmamış ve “local” olarak çalışmaktadır.

## Anahtar Kelimeler
Web geliştirme, frontend, backend, 
flask, bootstrap, indeksleme, veri, 
semantik analiz, benzerlik skorlaması, 
frekans

## I. Giriş
Bu projede web sitesi üzerinden kullanıcıdan URL’ler alınmış, ardından bu 
URL’lerdeki metin içerikleri kullanılarak 
web sitelerinde geçen kelimeler ve her kelimeye ait frekans değerleri bulunmuştur.
Bu frekans değerleri ve birkaç parametreye 
bağlı olarak anahtar kelime listesinin çıkarılması, çıkarılan anahtar kelimelere uygulanan bir formül yardımıyla benzerlik skoru bulunması işlemleri yapılmıştır. Ardından sitenin alt dallarının tespit edilmesiyle 
site yapısı ortaya çıkarılmış ve bu yapıdaki 
her URL’e aynı analizler uygulanmıştır.
Son olarak sitede aynı içerik içerisinde kullanılmış olan eş anlamlı sözcüklerin semantik analiz yardımıyla saptanması işlemi 
yapılmıştır. Kullanıcıların tüm bu işlemleri 
yapabilmesi için bir web sitesi tasarlanmıştır. İşlemler aşama aşama kullanıcının anlayacağı şekle getirilerek bilgi olarak bu
web sitesinde sunulmuştur.
Bu projede Python web framework’ü olan 
Flask, Bootstrap, internetten veri çekmek 
için BeautifulSoup ve Request kütüphanelerinin bir arada kullanımına yönelik bir 
çalışma gerçekleştirilmiştir. Aynı zamanda 
öğrencilerin, proje isterlerlerinin çözümününe yönelik araştırdığı algoritmalar IDE
aracılığıyla bilgisayar ortamına aktarılmıştır.

## II. Temel Bilgiler
Bu proje Python framework’ü Flask ile 
geliştirilmiş olup, geliştirme ortamı olarak 
"Visual Studio Code" kullanılmıştır. İlk 
etapta proje için bir yol haritası çıkarılarak 
ön hazırlık sürecine girilmiştir. Bu aşamada projenin isterlerine yönelik araştırmalar 
gerçekleştirilmesi adına grup içerisinde bir 
iş bölümü yapılmış olup elde edilen veriler 
doğrultusunda projenin ana hatları ortaya 
çıkarılmış ve büyük ölçüde karşılaşılabilecek problemler saptanıp çözümlendirilmeye çalışıldıktan sonra IDE ortamında projenin ilk adımları atılmıştır.
Yapılan ön hazırlık sürecinde web sitesi 
üzerinden URL’in alınması, alınan URL’in 
sahip olduğu metin içeriğinin işlenmesi, işlenen içerik üzerinden proje isterlerinin nasıl gerçekleştirilebileceği gibi problemler
üzerinde durulmuştur. Bu konulara ve
problemlere yönelik gerekli araştırmalar 
yapıldıktan sonra projeye şekil verme aşamasına gidilmiştir. 
Proje ön hazırlık süreciyle birlikte yaklaşık
on günlük bir süreçte tamamlanmıştır.

## III. Yöntem
Bu projede izlenilen yol aşağıda anlatılmıştır:

### Aşama 1
İlk olarak kullanıcıdan URL alınmıştır. 
Alınan URL bir fonksiyona gönderilerek 
sayfada geçen tüm kelimelerin frekansının 
bulunması işlemi yapılmıştır. Kullanıcıya 
sayfada geçen kelimeler frekanslarıyla beraber “büyükten küçüğe sıralanarak” listelenmiştir.

![Adsız](https://user-images.githubusercontent.com/65903573/113418572-70350100-93ce-11eb-902a-c8c3aaecdefe.png)

### Aşama 2-3
İkinci aşama üçüncü aşamanın ön hazırlığı 
niteliğinde olduğu için bu iki aşama web 
sitesinde tek bir sayfada sunulmuştur.
Birinci aşamadaki kelime frekansları bulma fonksiyonu ve “title” etiketi üzerinden
kelime bulma fonksiyonu kullanılarak bir 
anahtar kelime listesi bulma algoritması tasarlanmıştır. Ve tüm anahtar kelimeler alt 
alta listelenmiştir.

![Adsız](https://user-images.githubusercontent.com/65903573/113418813-e2a5e100-93ce-11eb-91bb-49242d7c1715.png)

Üçüncü aşamada ise listelenilen bu anahtar 
kelimelerden faydalanılarak benzerlik
skorlaması yapılmıştır. Benzerlik skorlamasında kullanılan formül şu şekildedir: <br>
a = ortak anahtar kelimelerin toplam 
frekans değeri <br>
b = tüm anahtar kelimelerin toplam 
frekans değeri <br>
x = benzerlik skoru <br>
x = (a / b) * 100

### Aşama 4-5
Beşinci aşama dördüncü aşamanın devamı 
niteliğinde olduğu için bu iki aşama web 
sitesinde tek bir sayfada sunulmuştur.
Dördüncü aşamada girilen URL ve URL 
kümesi arasında kümenin tüm birinci ve 
ikinci alt URL’leri de hesaba katılarak 
farklı bir benzerlik skorlaması bulma algoritması tasarlanmıştır.

![Adsız](https://user-images.githubusercontent.com/65903573/113419165-95763f00-93cf-11eb-831b-1fbc97cea5a6.png)

Beşinci aşamada, dördüncü aşamada 
kullanılan algoritmaya ek olarak 
incelemesi yapılan URL içeriğinde geçen 
eş anlamlı kelimelerin bulunmasını 
sağlayan algoritma kullanılmıştır. Bu 
kelimelerin “alakalı anahtar kelimeleri” 
anahtar kelimelerin yanlarına yazılmıştır.
Benzerlik skorlaması büyükten küçüğe 
sıralanmıştır.

![Adsız](https://user-images.githubusercontent.com/65903573/113419494-3b29ae00-93d0-11eb-91d5-f03ed0dd96c5.png)

Dördüncü ve beşinci aşamaya dair genel 
çıktı ek olarak sunulmuştur. *ek1

## IV. Kaba Kod
* Program çalıştı.
* Kullanıcı “Aşama 1” sekmesine gitti ve 
URL girişi yaparak “Ara” butonuna bastı.
* ”Aşama 1” için çıktı görüntülendi.
* Kullanıcı “Aşama 2|3” sekmesine gitti ve 
iki adet URL girişi yaparak “Ara” 
butonuna bastı.
* URL’ler alınarak gerekli fonksiyonlara 
gönderildi.
* Fonksiyonlardan döndürülen anahtar 
kelimelerin listesi, benzerlik skoruyla 
beraber web sitesinde gösterildi.
* Kullanıcı “Aşama 4|5” sekmesine gitti. 
Bir adet URL ve bir adet URL kümesi 
girdi (URL kümesi alt alta girilmelidir, 
aksi takdirde hata ile karşılaşılır.).
* Girilen URL’ler alt URL’leriyle birlikte 
“ağaç yapısı” şeklinde gösterildi.
* Her sitenin anahtar kelimeleri ve eğer 
sitede varsa eş anlamlı kelimeleri yan yana 
gösterildi.
* Alt URL’ler de kullanılarak bulunan 
benzerlik skoru gösterildi.

## ek1

![Adsız](https://user-images.githubusercontent.com/65903573/113419649-8774ee00-93d0-11eb-8adb-5d21fca891af.png)
![Adsız2](https://user-images.githubusercontent.com/65903573/113419664-9196ec80-93d0-11eb-90fc-781d6c6a061e.png) <br><br>
... çıktı girilen URL'lere göre bu şekilde devam etmektedir.

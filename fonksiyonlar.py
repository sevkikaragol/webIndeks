import requests
from bs4 import BeautifulSoup
import trStopWords
import operator

# -------------------------------------------------------------------------------------------------------------------------------------


def sembolTemizler(tumKelimeler):
    sembolsuzKelimeler = []
    semboller = "•!@$%^*()_{}\"<>,./;'&[’]-=·›:`~+|#?1234567890"
    # turkceKarakter= {"Ğ":"G","ğ":"g","Ü":"U","ü":"u","Ş":"S","İ":"I","Ö":"O","ö":"o","Ç":"C","ç":"c","ş":"s"}

    for kelime in tumKelimeler:

        kelime = kelime.replace("İ", "i")
        kelime = kelime.replace("I", "ı")

        kelime = kelime.lower()

        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol, "")

        if(len(kelime) > 0):
            sembolsuzKelimeler.append(kelime)

    return sembolsuzKelimeler

# -------------------------------------------------------------------------------------------------------------------------------------


def sozlukOlustur(tumKelimeler):
    kelimeSayisi = {}

    for kelime in tumKelimeler:
        if kelime in kelimeSayisi:
            kelimeSayisi[kelime] += 1
        else:
            kelimeSayisi[kelime] = 1

    return kelimeSayisi
# -------------------------------------------------------------------------------------------------------------------------------------


def kelimeFrekans(url):
    tumKelimeler = []

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    for kelimeGruplari in soup.find_all("body"):
        icerik = kelimeGruplari.text
        # print("************************ "+ icerik + " *********************************")
        # kelimeler = icerik.lower().split()
        kelimeler = icerik.split()

        for kelime in kelimeler:
            tumKelimeler.append(kelime)
            # print(kelime)

    tumKelimeler = sembolTemizler(tumKelimeler)

    # kelime silme esnasında sıranın kaybedilmemesi için listenin ilk halinin kopyası üzerinde geziyoruz.
    kopya = tumKelimeler.copy()

    for kelime in kopya:
        if(trStopWords.isStopWord(kelime)):
            tumKelimeler.remove(kelime)

    kelimeSayisi = sozlukOlustur(tumKelimeler)

    # kelimeSirali ->> frekansa göre sirali sözlük hali
    kelimeSirali = sorted(kelimeSayisi.items(),
                          key=operator.itemgetter(1), reverse=True)

    return kelimeSirali
# -------------------------------------------------------------------------------------------------------------------------------------


def anahtarKelime(sozluk, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    titleString = soup.title.string

    if soup.title.string is not None:
        titleString = soup.title.string.split()

        titleString = sembolTemizler(titleString)

        kopya = titleString.copy()

        for kelime in kopya:
            if(trStopWords.isStopWord(kelime)):
                titleString.remove(kelime)

    sayac = 0
    titleSayac = 0
    anahtarSozluk = []

    for kelime in sozluk:
        if (sayac == 5):
            break
        anahtarSozluk.append((kelime[0], kelime[1]))
        sayac += 1
    ornekList = list()
    for i, j in anahtarSozluk:
        ornekList.append(i)

    if soup.title.string is not None:
        for kelime in titleString:
            if titleSayac == 5:
                break
            if(kelime not in ornekList):
                anahtarSozluk.append((kelime, int(anahtarSozluk[0][1]*1/4)))
                titleSayac += 1

            if(kelime not in ornekList):
                ornekList.append(kelime)

    return anahtarSozluk
# -------------------------------------------------------------------------------------------------------------------------------------

# asama 3 icin kullanilmistir.


def benzerlikOrani(anahtarKelimeler, tumKelimeler):
    # gelen veriler liste seklindedir. [(),(),()]
    sayac = 0
    kelimeSayisi = 0
    for anahtarKelime in anahtarKelimeler:
        for kelime in tumKelimeler:
            if(anahtarKelime[0] == kelime[0]):
                sayac += (kelime[1]+anahtarKelime[1])

    for kelime in tumKelimeler:
        kelimeSayisi += kelime[1]

    for kelime in anahtarKelimeler:
        kelimeSayisi += kelime[1]

    return ((float(sayac)/float(kelimeSayisi))*100.0)

    # -------------------------------------------------------------------------------------------------------------------------------------


def asama4(anaUrl, siteKumesiString):

    genelListe = list()

# >>>>>>>>>>>>>>>>
    def child(url):
        if url.endswith("/"):
            url = url[0:len(url)-1]

        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        linkler = soup.find_all("a")
        liste = list()

        for link in linkler:
            if(str(link.get("href")).find(url) == 0):
                siteUrl = str(link.get("href"))

                if siteUrl.endswith("/"):
                    siteUrl = siteUrl[0:len(siteUrl)-1]

                if((siteUrl not in liste) and (url != siteUrl)):
                    liste.append(siteUrl)

        sayac = url.count("/")  # parent url '/' sayisi
        liste2 = list()

        for i in liste:  # i -> listede olan url'ler
            if (i.count("/") == sayac+1):
                liste2.append(i)

        return liste2
# >>>>>>>>>>>>>>>>>>>>>

    siteListesi = siteKumesiString.split("\n")
    a = 0
    for i in siteListesi:
        siteListesi[a] = siteListesi[a].replace("\r", "")
        a += 1


# buyuk dongu
    sozluk1 = anahtarKelime(kelimeFrekans(anaUrl), anaUrl)
    tumAnahtarKelimeler = list()

    for parentUrl in siteListesi:
        oran1 = 0
        oran2 = 0
        sozluk2 = anahtarKelime(kelimeFrekans(parentUrl), parentUrl)
        anaOran = round(benzerlikOrani(sozluk1, sozluk2), 2)
        # -------------------------aşama5-------------------------
        sozluk3 = list()
        hepsiList = kelimeFrekans(parentUrl)
        for anahtar, frekans in sozluk2:
            frekansSayaci = 0
            string = anahtar
            anlamliList = esBul(anahtar)
            for anlamli in anlamliList:
                for tumKelimeler in hepsiList:
                    if(anlamli == tumKelimeler[0]):
                        string = string+" ---> "+anlamli
                        frekansSayaci += 1
            sozluk3.append((string, frekans+frekansSayaci))
        sozluk3 = sorted(sozluk3, key=lambda x: x[1], reverse=True)

        # -------------------------aşama5-------------------------
        tumAnahtarKelimeler.append((parentUrl, sozluk3))

        childList1 = child(parentUrl)  # butun katmanlarin oldugu cocuklar
        childList2 = list()

        for firstChild in childList1:
            for i in child(firstChild):
                childList2.append(i)

        for cl1Url in childList1:
            cl1Anahtarlar = anahtarKelime(kelimeFrekans(cl1Url), cl1Url)
            oran1 += round(benzerlikOrani(sozluk1, cl1Anahtarlar), 2)
            # -------------------------aşama5-------------------------
            sozluk3 = list()
            hepsiList = kelimeFrekans(cl1Url)
            for anahtar, frekans in cl1Anahtarlar:
                frekansSayaci = 0
                string = anahtar
                anlamliList = esBul(anahtar)
                for anlamli in anlamliList:
                    for tumKelimeler in hepsiList:
                        if(anlamli == tumKelimeler[0]):
                            string = string+" ---> "+anlamli
                            frekansSayaci += 1
                sozluk3.append((string, frekans+frekansSayaci))
            sozluk3 = sorted(sozluk3, key=lambda x: x[1], reverse=True)

            # -------------------------aşama5-------------------------
            tumAnahtarKelimeler.append((cl1Url, sozluk3))

        if len(childList1) == 0:
            oran1 = 0
        else:
            oran1 = oran1/len(childList1)

        for cl2Url in childList2:
            cl2Anahtarlar = anahtarKelime(kelimeFrekans(cl2Url), cl2Url)
            oran2 += round(benzerlikOrani(sozluk1, cl2Anahtarlar), 2)
            # -------------------------aşama5-------------------------
            sozluk3 = list()
            hepsiList = kelimeFrekans(cl2Url)
            for anahtar, frekans in cl2Anahtarlar:
                frekansSayaci = 0
                string = anahtar
                anlamliList = esBul(anahtar)
                for anlamli in anlamliList:
                    for tumKelimeler in hepsiList:
                        if(anlamli == tumKelimeler[0]):
                            string = string+" ---> "+anlamli
                            frekansSayaci += 1
                sozluk3.append((string, frekans+frekansSayaci))
            sozluk3 = sorted(sozluk3, key=lambda x: x[1], reverse=True)

            # -------------------------aşama5-------------------------
            tumAnahtarKelimeler.append((cl2Url, sozluk3))

        if len(childList2) == 0:
            oran2 = 0
        else:
            oran2 = oran2/len(childList2)

        if len(childList1) == 0 and len(childList2) == 0:
            sonOran = anaOran
        else:
            sonOran = round((anaOran*16/21)+(oran1*4/21)+(oran2*1/21), 2)

        """for i,j in tumAnahtarKelimeler:
            print(i,"->",j)"""

        genelListe.append((parentUrl, sonOran, childList1, childList2))

    """print(genelListe)"""
    return (sorted(genelListe, key=lambda x: x[1], reverse=True), tumAnahtarKelimeler)  # sorts in place- asama4 fonksiyonu sonu


def esBul(kelime):
    url = "https://es-anlamli.gen.sx/?s=" + kelime
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    kelimeler = list()
    string = ""
    for k in soup.findAll('span', {'style': 'background: rgba(180,176,157,.15) none repeat scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; margin-left: 50px; color: blue; font-weight: bold;'}):
        string = k.text

    if(string == kelime):
        for k in soup.findAll('span', {'style': 'vertical-align:middle'}):
            string = k.text
            for i in string.split(","):
                kelimeler.append(i.strip(" "))

    return kelimeler


def agacYazdir(genelListe, anahtarlar):
    for i, j, k, l in genelListe:
        print(i, "-> ", j)
        for a, b in anahtarlar:
            if a == i:
                print(b)
        for x in k:
            print("    "+x)
            for a, b in anahtarlar:
                if a == x:
                    print(b)
            for y in l:
                if (y.find(x) == 0):
                    print("        "+y)
                    for a, b in anahtarlar:
                        if a == y:
                            print(b)

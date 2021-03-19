import requests
from bs4 import BeautifulSoup
import trStopWords
import operator

# -------------------------------------------------------------------------------------------------------------------------------------


def sembolTemizler(tumKelimeler):
    sembolsuzKelimeler = []
    semboller = "•!@$%^*()_{}\"<>,./;'&[’]-=·›:`~+|#?1234567890"
    #turkceKarakter= {"Ğ":"G","ğ":"g","Ü":"U","ü":"u","Ş":"S","İ":"I","Ö":"O","ö":"o","Ç":"C","ç":"c","ş":"s"}

    for kelime in tumKelimeler:

        kelime = kelime.replace("İ", "I")
        kelime = kelime.replace("ı", "i")
        kelime = kelime.replace("Ç", "C")
        kelime = kelime.replace("Ö", "O")
        kelime = kelime.replace("Ğ", "G")
        kelime = kelime.replace("Ş", "S")
        kelime = kelime.replace("Ü", "U")
        kelime = kelime.replace("ç", "c")
        kelime = kelime.replace("ö", "o")
        kelime = kelime.replace("ğ", "g")
        kelime = kelime.replace("ş", "s")
        kelime = kelime.replace("ü", "u")

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
        #print("************************ "+ icerik + " *********************************")
        #kelimeler = icerik.lower().split()
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
    titleString = soup.title.string.split()
    titleString = sembolTemizler(titleString)

    kopya = titleString.copy()

    for kelime in kopya:
        if(trStopWords.isStopWord(kelime)):
            titleString.remove(kelime)

    sayac = 0
    anahtarSozluk = []

    for kelime in sozluk:
        if (sayac == 5):
            break
        anahtarSozluk.append((kelime[0], kelime[1]))
        sayac += 1
    ornekList = list()
    for i, j in anahtarSozluk:
        ornekList.append(i)

    for kelime in titleString:
        if(kelime not in ornekList):
            anahtarSozluk.append((kelime, int(anahtarSozluk[0][1]*1/4)))

    return anahtarSozluk
# -------------------------------------------------------------------------------------------------------------------------------------


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

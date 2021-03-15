import requests
from bs4 import BeautifulSoup
import trStopWords
import operator




def kelimeFrekans(url):
    tumKelimeler = []

    def sembolTemizler(tumKelimeler):
        sembolsuzKelimeler = []
        semboller = "!@$%^*()_{}\"<>,./;'[]-=:`~+|#?1234567890"
        for kelime in tumKelimeler:
            for sembol in semboller:
                if sembol in kelime:
                    kelime = kelime.replace(sembol,"")

            if(len(kelime) > 0):
                sembolsuzKelimeler.append(kelime)

        return sembolsuzKelimeler

    r = requests.get(url)


    soup = BeautifulSoup(r.content,"html.parser")

    for kelimeGruplari in soup.find_all("p"):
        icerik = kelimeGruplari.text
        #print("************************ "+ icerik + " *********************************")
        kelimeler = icerik.lower().split()


        for kelime in kelimeler:
            tumKelimeler.append(kelime)
            #print(kelime)

    tumKelimeler = sembolTemizler(tumKelimeler)

    #kelime silme esnasında sıranın kaybedilmemesi için listenin ilk halinin kopyası üzerinde geziyoruz.
    kopya = tumKelimeler.copy()

    for kelime in kopya:
        if(trStopWords.isStopWord(kelime)):
            tumKelimeler.remove(kelime)



    #for i in tumKelimeler:
    # print(i)

    def sozlukOlustur(tumKelimeler):
        kelimeSayisi = {}

        for kelime in tumKelimeler:
            if kelime in kelimeSayisi:
                kelimeSayisi[kelime] += 1
            else:
                kelimeSayisi[kelime] = 1

        return kelimeSayisi


    kelimeSayisi = sozlukOlustur(tumKelimeler)

    #kelimeSirali ->> frekansa göre sirali sözlük hali
    kelimeSirali = sorted(kelimeSayisi.items(),key = operator.itemgetter(1),reverse = True)

    return kelimeSirali


def anahtarKelime(sozluk):
    sayac = 0
    anahtarSozluk = {}

    for kelime in sozluk:
        if (sayac==5):
            break

        anahtarSozluk[kelime[0]] = kelime[1]
        sayac+=1
    return anahtarSozluk
        






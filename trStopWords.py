#Durak kelimeler 'Information Retrieval on Turkish Texts' makalesinden alınmıştır.
#http://repository.bilkent.edu.tr/handle/11693/23211

stopWords = ["ama","boyle","dolayisiyla","her","ki","olmak","sadece","yaptigi",
"ancak","boylece","edecek","herhangi","kim","olmasi","siz","yaptigini",
"arada","bu","eden","herkesin","kimse","olmayan","sey","yaptiklari",
"ayrica","buna","ederek","hic","mi","olmaz","soyle","yerine",
"bana","bundan","edilecek","hicbir","mi","olsa","yine",
"bazi","bunlar","ediliyor","icin","mu","olsun","sunlari","yoksa",
"belki","bunlari","edilmesi","ile","mu","olup","tarafindan","zaten",
"ben","bunlarin","ediyor","ilgili","nasil","olur","uzere",
"beni","bunu","eger","ise","ne","olursa","var",
"benim","bunun","etmesi","iste","neden","oluyor","vardi",
"beri","burada","etti","itibaren","nedenle","ona","ve",
"bile","cok","ettigi","itibariyle","o","onlar","veya",
"bir","cunkü","ettigini","kadar","olan","onlari","ya",
"bircok","da","gibi","karsin","olarak","onlarin","yani",
"biri","daha","gore","kendi","oldu","onu","yapacak",
"birkac","de","halen","kendilerine","oldugu","onun","yapilan",
"biz","degil","hangi","kendini","oldugunu","oyle","yapilmasi",
"bize","diger","hatta","kendisi","olduklarini","oysa","yapiyor",
"bizi","diye","hem","kendisine","olmadi","pek","yapmak",
"bizim","dolayi","henuz","kendisini","olmadiği","ragmen","yapti","en","kac"]

def isStopWord(parameter):
    for word in stopWords:
        if(word == parameter):
            return True

    return False

from flask import Flask, render_template, request, flash
import fonksiyonlar as fs


app = Flask(__name__)
app.secret_key = "webIndex"

# index.html


@app.route("/")
def index():

    return render_template("index.html")
# index.html son


# asama1
@app.route("/asama1")
def asama1():

    return render_template("asama1.html", kontrol=False)


@app.route('/asama1', methods=['POST'])
def getValue():
    url = request.form['text-url']

    if (len(url) == 0):
        flash("Lütfen URL girişi yapınız.", "danger")
        return render_template("asama1.html", kontrol=False)

    sozluk = fs.kelimeFrekans(url)
    return render_template("asama1.html", kontrol=True, sozluk=sozluk)

 # asama1


# asama23
@app.route("/asama23")
def asama23():
    return render_template("asama23.html", kontrol=False)


@app.route('/asama23', methods=['POST'])
def getValue23():
    url1 = request.form['url1']
    url2 = request.form['url2']

    if (len(url1) == 0 or len(url2) == 0):
        flash("Lütfen URL girişi yapınız.", "danger")
        return render_template("asama23.html", kontrol=False)

    sozluk1 = fs.anahtarKelime(fs.kelimeFrekans(url1), url1)
    sozluk2 = fs.anahtarKelime(fs.kelimeFrekans(url2), url2)

    oran = round(fs.benzerlikOrani(sozluk1, sozluk2), 2)

    return render_template("asama23.html", kontrol=True, sozluk1=sozluk1, sozluk2=sozluk2, oran=oran)


# asama23


# asama45
@ app.route("/asama4")
def asama4():
    return render_template("asama4.html")


@ app.route('/asama4', methods=['POST'])
def getValue4():

    url1 = request.form['url1']
    url2 = request.form['url2']

    if (len(url1) == 0 or len(url2) == 0):
        flash("Lütfen URL girişi yapınız.", "danger")
        return render_template("asama4.html", kontrol=False)

    agacListe = fs.asama4(url1, url2)
    # fs.agacYazdir(agacListe[0],agacListe[1])

    return render_template("asama4.html", kontrol=True, agacListe=agacListe[0], anahtarKelimeler=agacListe[1])


# asama45


if __name__ == "__main__":
    app.run(debug=True)

from distutils.log import debug
from flask import Flask,render_template


app  = Flask(__name__)

@app.route("/")
def index():
    sayi = 10
    sayi2 = 20
    article = dict()
    article["title"] = "Book Title"
    article["body"] = "Book Body"
    article["author"] = "Book Author"
    return render_template("index.html",number = sayi, number2 = sayi2, article = article)

@app.route('/about')
def about():
    return "Hakkımda"

@app.route('/about/omer')
def omercan():
    return "Omer"

def method_name():
    pass

def method_name():
    pass

def method_name():
    pass
if __name__ == "__main__":
    app.run(debug=True)
    

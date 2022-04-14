from unicodedata import name
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    articles =[
        {"id":1,"title":"Deneme1","content":"Deneme1 content"},
        {"id":2,"title":"Deneme2","content":"Deneme2 content"},
        {"id":3,"title":"Deneme3","content":"Deneme3 content"}   
        ]
    return render_template("index.html",  articles = articles)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    return render_template("articles.html")

if __name__ == "__main__":
    app.run(debug=True)
    
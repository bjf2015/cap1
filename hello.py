from flask import Flask

app = Flask(__name__, static_url_path='')

@app.route("/hello")
def hello():
    return ("index.html")

if __name__== "__main__":
    app.run()

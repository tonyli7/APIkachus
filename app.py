import urllib2, json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/p")
@app.route("/p/<tag>")
def p(tag = "1"):
    url = """

"""
    url = url%(tag)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)


@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port 8000)

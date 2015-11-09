import urllib2, json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/p")
@app.route("/p/<tag>")
def p(tag = "1"):
    url = """
    http://pokeapi.co/api/v1/pokemon/%s
    """
    url = url%(tag)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    moves = []
    for item in r["moves"]:
        try:
            newitem = item["name"]
            moves.append(newitem)
        except:
            pass
    return render_template("tagged.html", data = moves)


@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port 8000)

import urllib2,json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/pokemon")
@app.route("/pokemon/<tag>")
def pokemon(tag="1"):
    url = """
    http://pokeapi.co/api/v1/pokemon/%s
    """
    url = url%(tag)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    abilities=[]
    for item in r['abilities']:
        try:
            newabilities = item['name']
            abilities.append(newabilities)
        except:
            pass
    return render_template("tagged.html",stuff=abilities)
    
@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)

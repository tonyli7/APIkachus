import urllib2,json
from flask import Flask, render_template, request
import utils


POKELIST=utils.getPokeList()
app = Flask(__name__)



@app.route("/pokemon", methods=["GET","POST"])
@app.route("/pokemon/<tag>")
def pokemon(tag=""):
    url = """
    http://pokeapi.co/api/v1/pokemon/%s
    """
  
    
    if tag=="":
        if request.method=="GET":
            return render_template("search.html")
        else:
            pokemon=request.form["pokemon"].lower()
            if utils.isValidPokemon(pokemon,POKELIST):
                tag=POKELIST.index(pokemon)+1
                url = url%(tag)
                request_url = urllib2.urlopen(url)
                result = request_url.read()
                r = json.loads(result)
                return render_template("tagged.html", r=r['name'].lower())
            else:
                error="Not a valid Pokemon"
                return render_template("search.html", error=error)
    else:
        url = url%(tag)
        request_url = urllib2.urlopen(url)
        result = request_url.read()
        r = json.loads(result)
        return render_template("tagged.html", r=r['name'].lower())
   # abilities=[]
   # for item in r['abilities']:
   #     try:
   #         newabilities = item['name']
   #         abilities.append(newabilities)
   #     except:
   #         pass
   # return render_template("tagged.html",stuff=abilities, r=r['name'].lower())
    
@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)

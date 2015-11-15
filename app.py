import urllib2,json
from flask import Flask, render_template, request, redirect
import utils


POKELIST=utils.getPokeList()
app = Flask(__name__)



@app.route("/pokemon", methods=["GET","POST"])
@app.route("/pokemon/<tag>")
def pokemon(tag=""):
    url = """
    http://pokeapi.co/api/v1/pokemon/%s
    """
    if tag=="":#if the tag is empty
        if request.method=="GET":
            return render_template("search.html")#search
        else:
            pokemon=request.form["pokemon"].lower()#stores a lowercase string pokemon
            if utils.isValidNumber(pokemon):
                return redirect("/pokemon/" + str(pokemon) )
            elif utils.isValidPokemon(pokemon,POKELIST):#checks if pokemon is valid
                tag=POKELIST.index(pokemon)+1#pokemon dex number
                url = url%(tag)
                request_url = urllib2.urlopen(url)
                result = request_url.read()
                r = json.loads(result)
                return redirect("/pokemon/"+str(tag))
            else:#if not a valid pokemon
                error="Not a valid Pokemon"
                return render_template("search.html", error=error)
    else:#if tag is not empty
        url = url%(tag)
        request_url = urllib2.urlopen(url)
        result = request_url.read()
        r = json.loads(result)
        return render_template("tagged.html",
                               types=r['types'],
                               name=r['name'].lower(),
                               species=r['species'],
                               move=r["moves"][(random.randrange(len(r["moves"])))]['name'].lower())
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

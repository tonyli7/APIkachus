import urllib2,json

def isValidPokemon(pkmn, pokelist):
    if pkmn in pokelist:
        return True
    return False


def getPokeList():
    file_=open("pokemon.csv","r")
    pkmnlines=file_.readlines()
    pokedata=[]
    pklist=[]
    for line in pkmnlines:
        pokedata+=[line.split(",")]
    for data in pokedata[1:]:
        pklist+=[data[1]]
    return pklist

   




def isValidPokemon(pkmn, pokelist):
    """
    PARAMS:
 
    pkmn is a string of a pokemon

    pokelist is a list of all the pokemon

    RETURNS:
     
    True if the pkmn is in the list

    False if the pkmn is not in the list
    """
    
    if pkmn in pokelist:
        return True
    return False


def getPokeList():
    """
    RETURNS:
    
    A list of strings of all the pokemon
    """
  
    file_=open("pokemon.csv","r")
    pkmnlines=file_.readlines()
    pokedata=[]
    pklist=[]
    for line in pkmnlines:
        pokedata+=[line.split(",")]
    for data in pokedata[1:]:
        pklist+=[data[1]]
    return pklist

   
def isValidNumber(thestring):
    if thestring.isDigit():
        if int(thestring) > 718:
            return False
    else:
        return False
    return True

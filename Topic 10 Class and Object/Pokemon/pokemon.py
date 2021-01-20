class Pokemon(object):
    def __init__(self, name, type, effectiveAgainst):
        self.name = name
        self.type = type
        self.effectiveAgainst = effectiveAgainst

    def isEffectiveAgainst(self, anotherPokemon):
        return self.effectiveAgainst == anotherPokemon.type

def initializePokemons():
        pokemon = []

        pokemon.append(Pokemon("Balbasaur", "leaf", "water"))
        pokemon.append(Pokemon("Pikatchu", "electric", "water"))
        pokemon.append(Pokemon("Charizard", "fire", "leaf"))
        pokemon.append(Pokemon("Balbasaur", "water", "fire"))
        pokemon.append(Pokemon("Kingler", "water", "fire"))

        return pokemon

pokemon = initializePokemons()
print(pokemon)

# Every pokemon has a name and a type.
# Certain types are effective against others, e.g. water is effective against fire.

# Ash has a few pokemon.
# A wild pokemon appeared!

wildPokemon = Pokemon ("Oddish", "leaf", "water")
wildPokemon2 = Pokemon ("Balbasaur", "leaf", "water")
wildPokemon3 = Pokemon ("Pikatchu", "electric", "water")
wildPokemon4 = Pokemon ("Charizard", "fire", "leaf")
wildPokemon5 = Pokemon ("Kingler", "water", "fire")

my_pok = Pokemon("temp1","temp2","temp3")


# Which pokemon should Ash use?
for pok in pokemon:
    if pok.effectiveAgainst == wildPokemon.type:
        my_pok = pok
print("I choose you, " + my_pok.name )
# print (my_pok.isEffectiveAgainst(wildPokemon))
# print (my_pok.isEffectiveAgainst(wildPokemon2))
# print (my_pok.isEffectiveAgainst(wildPokemon3))
# print (my_pok.isEffectiveAgainst(wildPokemon4))
# print (my_pok.isEffectiveAgainst(wildPokemon5))
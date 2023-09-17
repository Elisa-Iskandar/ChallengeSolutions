#Task:

#You are given a list of pokemon caught, the issue is some of them are duplicates which don’t need to be counted towards the number of unique pokemon caught. 

#You are first given an integer n, the number of Pokemons. You are then given the list of Pokemons. 

#Determine the number of unique Pokemons. 
n = int(input("n: "))
pokemon = []
for x in range(n):
  pokemon_input = input("pokemon: ")
  pokemon.append(pokemon_input)

pokemon.sort()

final = []
prev = None
for y in range(len(pokemon)):
  if pokemon[y] != prev:
    final.append(pokemon[y])
  prev = pokemon[y]


print(len(final))


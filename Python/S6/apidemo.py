import requests

response=requests.get("https://pokeapi.co/api/v2/pokemon")
data=response.json()
listaPokemones=data['results']

urldetalle="https://pokeapi.co/api/v2/pokemon/"

for i,index in enumerate(listaPokemones):
    print(f"{i+1}){index['name']}")
    

pokemonSeleccionado=input("ingresa el numero del pokemon a querer ver su detalle")
urlPokemon=f"https://pokeapi.co/api/v2/pokemon/{pokemonSeleccionado}/"
print(urlPokemon)

response=requests.get(urlPokemon)
pokemon=response.json()

print(pokemon)
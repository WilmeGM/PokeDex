# Script Module: pokemon_utils

def build_pokemon_cards(pokemons, isFiltered=False):
    """
    Receives a list of Pokémon and returns a list of cards.
		- pokemons: List of dictionaries (from the API or filteredPokemons)
		- isFiltered: True if the Pokémon are filtered (using 'name').
		False if they are from results (using 'url').
    """
    instances = []
    for p in pokemons:
        try:
            if isFiltered:
                name = p["name"]
                poke_url = "https://pokeapi.co/api/v2/pokemon/{}".format(name)
            else:
                poke_url = p["url"]
            
            detail_response = system.net.httpGet(poke_url)
            detail_body = system.util.jsonDecode(detail_response)
            
            pokemon_type1 = detail_body["types"][0]["type"]["name"]
            if len(detail_body["types"]) == 2:
                pokemon_type2 = detail_body["types"][1]["type"]["name"]
                pokemon_types = [{"name": pokemon_type1}, {"name": ", " + pokemon_type2}]
            else:
                pokemon_types = [{"name": pokemon_type1}, {"name": ""}]
            
            card = {
                "id": detail_body["id"],
                "name": detail_body["name"],
                "image_url": detail_body["sprites"]["front_default"] or "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png",
                "types": pokemon_types,
                "hp": detail_body["stats"][0]["base_stat"],
                "attack": detail_body["stats"][1]["base_stat"],
                "defense": detail_body["stats"][2]["base_stat"],
                "speed": detail_body["stats"][5]["base_stat"]
            }
            
            instances.append(card)
        
        except Exception as e:
            system.perspective.print("Error en build_pokemon_cards: " + str(e))
    
    return instances

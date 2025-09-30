def runAction(self, event):
    try:
        limit = self.getSibling("LimitNumericEntryField").props.value
        
        gen_url = self.getSibling("GenerationsDropdown").props.value
        
        self.getSibling("PokemonsFlexRepeater").props.instances = []
            
        gen_response = system.net.httpGet(gen_url)
        gen_body = system.util.jsonDecode(gen_response)
        pokemons = gen_body["pokemon_species"]
            
        self.parent.custom.filteredPokemons = pokemons
            
        self.parent.custom.currentPage = 0
        self.parent.custom.startIndex = self.parent.custom.currentPage * limit
        self.parent.custom.endIndex = self.parent.custom.startIndex + limit
        
        from pokemon_utils import build_pokemon_cards
        pokemons = pokemons[:limit]
        instances = build_pokemon_cards(pokemons, isFiltered=True)
        self.getSibling("PokemonsFlexRepeater").props.instances = instances
        self.getSibling("NoFilterPagesLabel").meta.visible = False
        self.getSibling("FilteredPagesLabel").meta.visible = True
        
    except Exception as e:
        system.perspective.print("Error: " + str(e))

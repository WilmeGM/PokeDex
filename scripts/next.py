def runAction(self, event):
    try:
    	gen_url = self.getSibling("GenerationsDropdown").props.value
    	
    	if gen_url:
			pokemons = self.parent.custom.filteredPokemons
			
			if self.parent.custom.endIndex >= len(pokemons):
				return
			
			self.parent.custom.currentPage += 1
			
			self.parent.custom.startIndex = self.parent.custom.currentPage * 5
			self.parent.custom.endIndex = self.parent.custom.startIndex + 5
			
			self.parent.custom.visibleItems = pokemons[self.parent.custom.startIndex:self.parent.custom.endIndex]
			
			self.getSibling("PokemonsFlexRepeater").props.instances = []
			
			from pokemon_utils import build_pokemon_cards
			instances = build_pokemon_cards(self.parent.custom.visibleItems, isFiltered=True)
        else:
			self.getSibling("PokemonsFlexRepeater").props.instances = []
			
			next_url = self.parent.custom.nextUrl
			if not next_url:
				return
			
			self.parent.custom.currentUrl = next_url
			offset = int(self.parent.custom.currentUrl.split("offset=")[1].split("&")[0]) if "offset=" in self.parent.custom.currentUrl else 0
			self.parent.custom.currentPageNoFilter = int(offset / 5)
			
			response = system.net.httpGet(next_url)
			body = system.util.jsonDecode(response)
			
			self.parent.custom.nextUrl = body["next"]
			self.parent.custom.prevUrl = body["previous"]
			
			from pokemon_utils import build_pokemon_cards
			pokemons = body["results"]
			instances = build_pokemon_cards(pokemons, isFiltered=False)
				
        self.getSibling("PokemonsFlexRepeater").props.instances = instances
    except Exception as e:
    	system.perspective.print("Error: " + str(e))

def runAction(self, event):
  	try:
		self.getSibling("NoFilterPagesLabel").meta.visible = True
		self.getSibling("FilteredPagesLabel").meta.visible = False
		
		self.getSibling("GenerationsDropdown").props.value = None
		self.getSibling("FiltersButton").props.enabled = False
		
		self.getSibling("PokemonsFlexRepeater").props.instances = []
		
		url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=5"
		
		self.parent.custom.currentUrl = url
		
		response = system.net.httpGet(url)
		body = system.util.jsonDecode(response)
		
		self.parent.custom.nextUrl = body["next"]
		self.parent.custom.prevUrl = body["previous"]
		self.parent.custom.currentPage = 0
		offset = int(self.parent.custom.currentUrl.split("offset=")[1].split("&")[0]) if "offset=" in self.parent.custom.currentUrl else 0
		self.parent.custom.currentPageNoFilter = int(offset / 5)
		
		from pokemon_utils import build_pokemon_cards
		pokemons = body["results"]
		instances = build_pokemon_cards(pokemons, isFiltered=False)
		self.getSibling("PokemonsFlexRepeater").props.instances = instances
		
		gen_url = "https://pokeapi.co/api/v2/generation/"
		gen_response = system.net.httpGet(gen_url)
		gen_body = system.util.jsonDecode(gen_response)
		
		for g in gen_body["results"]:
			options.append({
        		"label": g["name"],  
        		"value": g["url"]                
    		})
		
		self.getSibling("GenerationsDropdown").props.options = options
	except Exception as e:
		print("Error: " + str(e))

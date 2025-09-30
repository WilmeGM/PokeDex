def runAction(self):
  	try:
		self.getChild("root").getChild("NoFilterPagesLabel").meta.visible = True
		self.getChild("root").getChild("FilteredPagesLabel").meta.visible = False
		self.getChild("root").getChild("PokemonsFlexRepeater").props.instances = []
		
		url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=5"
		
		self.getChild("root").custom.currentUrl = url
		
		response = system.net.httpGet(url)
		body = system.util.jsonDecode(response)
		
		self.getChild("root").custom.count = body["count"]
		self.getChild("root").custom.nextUrl = body["next"]
		self.getChild("root").custom.prevUrl = body["previous"]
		self.getChild("root").custom.currentPage = 0
		import math
		self.getChild("root").custom.totalPages = int(math.ceil(body["count"] / float(5)))
		offset = int(self.getChild("root").custom.currentUrl.split("offset=")[1].split("&")[0]) if "offset=" in self.getChild("root").custom.currentUrl else 0
		self.getChild("root").custom.currentPageNoFilter = int(offset / 5)
		
		from pokemon_utils import build_pokemon_cards
		pokemons = body["results"]
		instances = build_pokemon_cards(pokemons, isFiltered=False)
		self.getChild("root").getChild("PokemonsFlexRepeater").props.instances = instances
		
		gen_url = "https://pokeapi.co/api/v2/generation/"
		gen_response = system.net.httpGet(gen_url)
		gen_body = system.util.jsonDecode(gen_response)
		options = []
		
		for g in gen_body["results"]:
			options.append({
        		"label": g["name"],  
        		"value": g["url"]                
    		})
		
		self.getChild("root").getChild("GenerationsDropdown").props.options = options
	except Exception as e:
		print("Error: " + str(e))

# PokeDex

This project is a **Pokémon browser** built with **Ignition Perspective** and powered by the [PokéAPI](https://pokeapi.co/).  
It demonstrates how to fetch, filter, and display Pokémon data in a modern and interactive interface.

---

## 📌 Features

- 🔄 **Pagination (Next / Previous)** for browsing all Pokémon.  
- 🎯 **Filtering by Generation** (e.g., Generation I, II, III, etc.).  
- 🃏 **Dynamic Pokémon Cards** with:  
  - Name  
  - ID  
  - Sprite (default image or fallback)  
  - Types (one or two types per Pokémon)  
  - Stats: HP, Attack, Defense, Speed  
- 📊 **Page indicators**:  
  - Standard browsing (`Page X of Y`)  
  - Filtered browsing (`Page X of Y` with generation results)  
- ⚡ **Reusable Script Module** (`pokemon_utils`) to build Pokémon cards from API results.  

---

## 🛠️ Project Structure

### 1. **Script Module: `pokemon_utils.py`**  
Handles the logic to build Pokémon cards by calling the detail endpoint from PokéAPI.  

```python
def build_pokemon_cards(pokemons, isFiltered=False):
    """
    Receives a list of Pokémon and returns a list of cards.
    - pokemons: List of dictionaries (from API or filtered list)
    - isFiltered: True if the Pokémon list comes from generation (uses 'name'),
                  False if it comes from standard browsing (uses 'url').
    """
```

### 2. **Startup Script (`onStartup`)**  
- Loads the **first page** of Pokémon with `offset=0&limit=5`.  
- Initializes:  
  - Current page  
  - Total pages  
  - Next / Previous URLs  
- Fetches the list of **generations** and populates the dropdown.  

### 3. **Apply Filters**  
- Uses the selected generation from the dropdown.  
- Filters Pokémon species by generation.  
- Paginates results manually with `startIndex` and `endIndex`.  
- Shows the filtered page indicator.  

### 4. **Pagination (Next / Previous)**  
- For **no filter**: uses API URLs (`next`, `previous`) and `offset`/`limit`.  
- For **filtered browsing**: uses manual slicing of the list (`currentPage * limit`).  

---

## 🚀 How to Run

1. Open **Ignition Designer**.  
2. Import this project.  
3. Launch the **Perspective session**.  
4. Start browsing Pokémon:  
   - Use **Next / Previous** to move through the standard list.  
   - Select a **Generation** from the dropdown and apply filters.  

---

## 📸 Preview (Example)
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/55a66a29-97f3-4259-9be2-916a34db920d" />
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/d3e404f2-d716-41d5-92a8-fd1c0fbb1554" />
<img width="1918" height="865" alt="image" src="https://github.com/user-attachments/assets/402b6a99-e68e-4ae3-a7ce-d68ec2c01d06" />

Pokémon and related content are © Nintendo, Game Freak, and The Pokémon Company.  
PokéAPI is a free and open-source RESTful API for Pokémon data.  

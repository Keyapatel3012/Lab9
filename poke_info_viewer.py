""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox
import requests
# Create the main window
root = Tk()
root.title("Pokemon Information")

# TODO: Create the frames
frame_input = ttk.Frame(root)
frame_input.grid(row=0, column=0, columnspan=2, pady=(20,10))

frame_info = ttk.LabelFrame(root, text="Info")
frame_info.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

frame_stats = ttk.LabelFrame(root, text="stats")
frame_stats.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

label_name = ttk.Entry(frame_input, text="Pokemon Name")
label_name.grid(row=0, column=0, padx=(10,5), pady=(10,))

enter_name = ttk.Entry(frame_input)
enter_name.insert(0,'mew')
enter_name.grid(row=0, column=1) 

# TODO: Define button click event handler function
def handle_button_get_info():
   poke_name = enter_name.get().strip()
   if poke_name == '' : return
   poke_info = get_pokemon_info(poke_name)

   if poke_info:
      # Populate the Info frame
        label_height_value.config(text=f"Height: {poke_info['height']} dm")
        label_weight_value.config(text=f"Weight: {poke_info['weight']} hg")
        label_types_value.config(text=f"Type(s): {', '.join(poke_info['types'])}")

        # Populate the Stats frame
        special_attack_bar["value"] = poke_info['stats']['special_attack']
        special_defense_bar["value"] = poke_info['stats']['special_defense']
        speed_bar["value"] = poke_info['stats']['speed']

       
   else:
       messagebox.showerror("Error", f"Failed to retrieve Pokémon information for {poke_name.capitalize()}.")

button_get_info = ttk.Button(frame_input, text="Get Info", command=handle_button_get_info)
button_get_info.grid(row=0, column=2, padx=(5, 10))

# TODO: Populate the user input frame with widgets
label_height_value = ttk.Label(frame_info, text="")
label_height_value.grid(row=0, column=0, padx=5, pady=2, sticky=W)

label_weight_value = ttk.Label(frame_info, text="")
label_weight_value.grid(row=1, column=0, padx=5, pady=2, sticky=W)

label_types_value = ttk.Label(frame_info, text="")
label_types_value.grid(row=2, column=0, padx=5, pady=2, sticky=W)

special_attack_bar = ttk.Progressbar(frame_stats, length=100, mode="determinate")
special_attack_bar.grid(row=0, column=0, padx=5, pady=2)

special_defense_bar = ttk.Progressbar(frame_stats, length=100, mode="determinate")
special_defense_bar.grid(row=1, column=0, padx=5, pady=2)

speed_bar = ttk.Progressbar(frame_stats, length=100, mode="determinate")
speed_bar.grid(row=2, column=0, padx=5, pady=2)




root.mainloop()
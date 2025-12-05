import gui
import logic
import pyperclip
import json

with open("settings.json","r") as file:
    settings = json.load(file)
    
#windows config
WIDTH = settings["window"]["width"]
HEIGHT = settings["window"]["height"]

#grid Settings
GS = settings["grid"]
ROWS = GS["rows"]
COLS = GS["height"]
SCATTERING = GS["scattering"]
SIZE = GS["size"]
STATES = [[0 for _ in range(ROWS)] for _ in range(COLS)]
COLORS = GS["colors"]

max = 3

#current_facing = i

kara = settings["kara"]



pyperclip.copy("\n".join(logic.generate(gui.states, gui.kara)))
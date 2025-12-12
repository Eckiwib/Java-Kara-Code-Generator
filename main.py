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
COLS = GS["columns"]
SCATTERING = GS["scattering"]
SIZE = GS["size"]
STATES = [[0 for _ in range(ROWS)] for _ in range(COLS)]
COLORS = GS["colors"]
kara = settings["kara"]

max = 3

def generate(states, kara):
    generator = logic.generate(states, kara)
    for fac in range(4):
        check = generator.check(fac)
        if check > 0:
            cmds = generator.fac_cmd()
            generator.final()
            break
        
    pyperclip.copy("\n".join(cmds))

window = gui.window(w_size_x=WIDTH, w_size_y=HEIGHT, size=SIZE,rows=ROWS, cols=COLS, scattering=SCATTERING, states=STATES, colors=COLORS, kara=kara, generate=generate)
window.run()
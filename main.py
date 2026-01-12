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
COLORS = GS["colors"]
kara = settings["kara"]

STATES = [[0 for _ in range(ROWS)] for _ in range(COLS)]

max = 3

def generate(states, kara):
    generator = logic.generate(states, kara)
    fac = 0
    cmds = []
    while fac < 3:
        for fac in range(4):
            check = generator.check(fac)
            print(check)
            if check > 0:
                cmds.append(generator.fac_cmd())
                generator.final()
                break
    
    print(cmds)
    #pyperclip.copy("\n".join(cmds))

window = gui.window(w_size_x=WIDTH, w_size_y=HEIGHT, size=SIZE,rows=ROWS, cols=COLS, scattering=SCATTERING, states=STATES, colors=COLORS, kara=kara, generate=generate)
window.run()